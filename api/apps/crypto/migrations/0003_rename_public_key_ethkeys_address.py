# Generated by Django 4.1.3 on 2022-12-11 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_alter_ethkeys_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ethkeys',
            old_name='public_key',
            new_name='address',
        ),
    ]
