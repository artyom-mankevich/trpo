# Generated by Django 4.1.3 on 2022-12-09 21:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0013_alter_transaction_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=10, max_digits=30)),
                ('currency', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallets.wallet')),
            ],
        ),
    ]
