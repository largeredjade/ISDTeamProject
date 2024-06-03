from django.db import models
from products.models import Product
# Create your models here.

class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    warehouse_out_date = models.DateTimeField()
    shipment_status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.shipment_id)

class ShipmentDetail(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_arrival_date = models.DateTimeField()
    detail_qty = models.IntegerField()

    class Meta:
        unique_together = ('shipment', 'product')

    def __str__(self):
        return f'{self.shipment_id} - {self.product_id}'