# Generated by Django 4.1 on 2024-06-03 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("shipment", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="shipment",
            old_name="order_status",
            new_name="shipment_status",
        ),
        migrations.RemoveField(
            model_name="shipment",
            name="shipment_date",
        ),
        migrations.RemoveField(
            model_name="shipmentdetail",
            name="delivery_date",
        ),
        migrations.RemoveField(
            model_name="shipmentdetail",
            name="product_name",
        ),
        migrations.AddField(
            model_name="shipment",
            name="warehouse_outdate",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="shipmentdetail",
            name="customer_arrival_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]