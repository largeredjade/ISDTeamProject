from django.contrib import admin
from .models import Delivery, DeliveryDetail

admin.site.register(Delivery)
admin.site.register(DeliveryDetail)