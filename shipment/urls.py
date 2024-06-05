from django.urls import path


from shipment import views

urlpatterns = [
    path('', views.shipment_list, name = 'shipment_list'),
    path('detail/', views.shipment_detail_list, name = 'shipment_detail_list'),
    path('create/', views.create_shipment, name = 'create_shipment'),
    path('detail/create/', views.create_shipment_detail, name = 'create_shipment_detail'),
    path('update/<int:shipment_id>/', views.update_shipment, name = 'update_shipment'),
    path('<int:shipment_id>/detail/<int:product_id>/update/', views.update_shipment_detail, name='update_shipment_detail'),
    path('delete/<int:shipment_id>', views.delete_shipment, name = 'delete_shipment'),
    path('<int:shipment_id>/detail/<int:product_id>/delete/', views.delete_shipment_detail, name ='delete_shipment_detail'),
]
