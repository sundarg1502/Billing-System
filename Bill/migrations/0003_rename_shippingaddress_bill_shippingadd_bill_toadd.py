# Generated by Django 5.1.2 on 2025-01-15 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0002_bill_ewaybill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='shippingAddress',
            new_name='shippingAdd',
        ),
        migrations.AddField(
            model_name='bill',
            name='toAdd',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
    ]