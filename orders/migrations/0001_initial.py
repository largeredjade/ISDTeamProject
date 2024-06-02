# Generated by Django 4.1 on 2024-06-02 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("suppliers", "0001_initial"),
        ("Users", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("order_date", models.DateTimeField()),
                ("expected_arrivalDate", models.DateTimeField()),
                (
                    "order_totalCost",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("order_status", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Users.users"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("detail_qty", models.IntegerField()),
                ("discount", models.DecimalField(decimal_places=2, max_digits=5)),
                ("description", models.CharField(max_length=90)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orders.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="suppliers.supplier",
                    ),
                ),
            ],
            options={
                "unique_together": {("order", "product")},
            },
        ),
    ]
