# Generated by Django 5.1.2 on 2025-01-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0003_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='eWayBill',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='invNo',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='qty',
        ),
        migrations.AlterField(
            model_name='bill',
            name='items',
            field=models.CharField(max_length=20),
        ),
    ]