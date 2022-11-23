# Generated by Django 4.1.3 on 2022-11-23 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='is_debt',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='source_wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source_wallet_transactions', to='wallets.wallet'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='target_wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='target_wallet_transactions', to='wallets.wallet'),
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('user_id', models.CharField(db_index=True, max_length=64)),
                ('expires_at', models.DateField()),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallets.wallet')),
            ],
        ),
    ]
