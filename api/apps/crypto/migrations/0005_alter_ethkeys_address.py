# Generated by Django 4.1.3 on 2022-12-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0004_alter_ethkeys_private_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethkeys',
            name='address',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
