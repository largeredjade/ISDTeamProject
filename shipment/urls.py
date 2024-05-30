# shipment/urls.py
from django.urls import path
from .views import shipment_list

urlpatterns = [
    path('list/', shipment_list, name='shipment_list'),
]
