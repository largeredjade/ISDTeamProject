from django.shortcuts import render
from .models import Delivery
# Create your views here.
def delivery_create(request):
    return render(request, 'Delivery/../templates/html/delivery_create.html')
