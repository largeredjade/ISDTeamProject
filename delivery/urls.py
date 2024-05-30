# delivery/urls.py
from django.urls import path
from .views import views

urlpatterns = [
    path('create/', views.delivery_create, name='delivery_create'),
]
