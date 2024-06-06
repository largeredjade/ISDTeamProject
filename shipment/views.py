from django.shortcuts import render, get_object_or_404, redirect
from .models import Shipment, ShipmentDetail
from .forms import ShipmentDetailForm, ShipmentForm
# Create your views here.

def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'html/shipment_list.html', {'shipments': shipments})

def shipment_detail_list(request):
    shipment_detail = ShipmentDetail.objects.all()
    return render(request, 'html/shipment_detail_list.html', {'shipment_detail': shipment_detail})

def create_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipment_list')
    else:
        form = ShipmentForm()
    return render(request, 'html/shipment_create.html', {'form': form})

def create_shipment_detail(request):
    if request.method == 'POST':
        form = ShipmentDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipment_detail_list')  # or another appropriate view
    else:
        form = ShipmentDetailForm()
    return render(request, 'html/shipment_detail_create.html', {'form': form})


def update_shipment(request, shipment_id):
    shipment = Shipment.objects.get(shipment_id=shipment_id)
    form = ShipmentForm(request.Post or None, instance=shipment)
    if form.is_valid():
        form.save()
        return redirect('shipment_list')
    else:
        form = ShipmentDetailForm(instance=shipment)
    return render(request, 'html/shipment_update.html', {'form':form})
def update_shipment_detail(request, shipment_id, product_id):
    shipment_detail = get_object_or_404(ShipmentDetail, shipment_id=shipment_id, product_id=product_id)

    if request.method == 'POST':
        form = ShipmentDetailForm(request.POST, instance=shipment_detail)
        if form.is_valid():
            form.save()
            return redirect('shipment_detail_list', shipment_id=shipment_id)
    else:
        form = ShipmentDetailForm(instance=shipment_detail)

    return render(request, 'html/shipment_detail_update.html', {'form': form, 'shipment_detail': shipment_detail})

def delete_shipment(request, shipment_id):
    shipment = Shipment.objects.get(shipment_id=shipment_id)
    if request.method == 'POST':
        shipment.delete()
        return redirect('shipment_list')
    return render(request, 'html/shipment_delete.html', {'shipment': shipment})

def delete_shipment_detail(request, shipment_id, product_id):
    shipment_detail = ShipmentDetail.objects.get(shipment_id=shipment_id, product_id=product_id)
    if request.method == 'POST':
        shipment_detail.delete()
        return redirect('shipment_detail_list')
    return render(request, 'html/shipment_detail_delete.html', {'shipment_detail': shipment_detail})
