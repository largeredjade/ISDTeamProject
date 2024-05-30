from django.shortcuts import render

# Create your views here.
def shipment_list(request):
    return render(request, 'shipment/../templates/html/shipment_list.html')