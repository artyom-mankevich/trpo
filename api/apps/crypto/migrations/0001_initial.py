# Generated by Django 4.1.3 on 2022-11-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EthKeys',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('user_id', models.CharField(db_index=True, max_length=64)),
                ('private_key', models.CharField(max_length=128)),
                ('public_key', models.CharField(max_length=128)),
            ],
        ),
    ]
