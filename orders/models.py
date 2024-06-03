from django.db import models
from products.models import Product
from suppliers.models import Supplier
from Users.models import Users

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    expected_arrivaldate = models.DateTimeField()
    order_totalcost = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.order_id)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    detail_qty = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=50)
    supplier_sellingprice = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f'{self.order_id} - {self.product_id}'