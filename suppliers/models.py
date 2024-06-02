from django.db import models

# Create your models here.
class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=50)
    supplier_address = models.CharField(max_length=50)
    supplier_phoneNumber = models.CharField(max_length=50)

    def __str__(self):
        return self.supplier_name