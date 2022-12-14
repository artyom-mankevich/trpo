from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from accounts.views import SetUserIdFromTokenOnCreateMixin
from investments.models import Stock, Investment
from investments.serializers import StockSerializer, InvestmentSerializer
from investments.utils import set_stock_prices, get_stocks_chart_data


class StockViewSet(viewsets.ModelViewSet, SetUserIdFromTokenOnCreateMixin):
    serializer_class = StockSerializer

    pagination_class = PageNumberPagination

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pagination_class.page_size = 5

    def get_queryset(self):
        return Stock.objects.all().filter(user_id=self.request.user).order_by(
            "-created_at"
        )

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data["results"]:
            set_stock_prices(response.data["results"], str(request.user))

        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        set_stock_prices([response.data], str(request.user))

        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        set_stock_prices([response.data], str(request.user))

        return response

    @action(detail=False, methods=["get"], url_path="chart-data", url_name="chart-data")
    def chart_data(self, request, *args, **kwargs):
        period = request.query_params.get("period", Stock.CHART_PERIOD_7_DAYS)
        if period not in Stock.CHART_PERIODS:
            return Response(
                {"error": f"Period {period} is not allowed"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        stocks = (
            Stock.objects.filter(user_id=self.request.user)
            .values("ticker")
            .annotate(amount=Sum("amount"))
        )
        if stocks:
            stocks_dict = {stock["ticker"]: stock["amount"] for stock in stocks}
            return Response(
                data=get_stocks_chart_data(stocks_dict, period, str(request.user))
            )

        return Response(data={})


class InvestmentViewSet(viewsets.ModelViewSet, SetUserIdFromTokenOnCreateMixin):
    serializer_class = InvestmentSerializer

    def get_queryset(self):
        return Investment.objects.all().filter(user_id=self.request.user).order_by(
            "-created_at"
        )
