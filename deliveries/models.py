from django.db import models
from products.models import Product
from orders.models import Order
from Users.models import Users
from suppliers.models import Supplier

# Create your models here.

class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return str(self.delivery_id)

class DeliveryDetail(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    detail_qty = models.IntegerField()

    class Meta:
        unique_together = ('delivery', 'product')

    def __str__(self):
        return f'{self.delivery_id} - {self.product_id}'