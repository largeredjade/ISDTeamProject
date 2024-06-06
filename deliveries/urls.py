from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_list, name='delivery_list'),
    path('detail/', views.delivery_detail_list, name='delivery_detail_list'),
    path('create/', views.create_delivery, name='create_delivery'),
    path('detail/create/', views.create_delivery_detail, name='create_delivery_detail'),
    path('update/<int:delivery_id>/', views.update_delivery, name='update_delivery'),
    path('<int:delivery_id>/detail/<int:product_id>/<int:order_id>/<int:user_id>/update/', views.update_delivery_detail, name='update_delivery_detail'),
    path('delete/<int:delivery_id>/', views.delete_delivery, name='delete_delivery'),
    path('<int:delivery_id>/detail/<int:product_id>/<int:order_id>/<int:user_id>/delete/', views.delete_delivery_detail, name='delete_delivery_detail'),

]
