# Generated by Django 4.1.3 on 2022-12-06 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0006_remove_stock_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='stock',
            name='color',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='description',
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='investments.ticker'),
        ),
    ]
