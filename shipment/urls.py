from django.urls import path

from shipment import views

urlpatterns = [
    path('', views.shipment_list, name = 'shipment_list'),
    path('create/', views.create_shipment_detail, name = 'create_shipment'),
    path('shipment/<int:shipment_id>/detail/<int:product_id>/update/', views.update_shipment_detail, name='update_shipment_detail'),
    path('shipment/<int:shipment_id>/detail/<int:product_id>/delete/', views.delete_shipment_detail, name = 'delete_shipment_detail'),
]
