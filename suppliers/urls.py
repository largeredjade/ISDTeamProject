from django.urls import path

from suppliers import views

urlpatterns = [
    path('', views.supplier_list, name = 'supplier_list'),
    path('create/', views.create_supplier, name = 'create_supplier'),
    path('update/<int:supplier_id>/', views.update_supplier, name='update_supplier'),
    path('delete/<int:supplier_id>/', views.delete_supplier, name = 'delete_supplier'),
]
