# Generated by Django 5.1.2 on 2025-03-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0005_alter_bill_gstin'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='tt_scrap',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
