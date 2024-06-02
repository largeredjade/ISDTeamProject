from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_volume = models.CharField(max_length=50)
    product_qty = models.IntegerField()
    product_weight = models.DecimalField(max_digits=10, decimal_places=2)
    product_minQty = models.IntegerField()
    product_location = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    maintenance_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
