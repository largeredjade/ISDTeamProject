from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('<int:order_id>/update/', views.order_update, name='order_update'),
    path('<int:order_id>/delete/', views.order_delete, name='order_delete'),

    path('detail/',views.order_detail_list, name = 'order_detail_list'),

    path('detail/create/', views.order_detail_create, name = 'order_detail_create'),
    path('<int:order_id>/<int:supplier_id>/<int:product_id>/update', views.order_detail_create, name='order_detail_update'),
    path('<int:order_id>/<int:supplier_id>/<int:product_id>/delete', views.order_detail_delete, name='order_detail_delete')
]


