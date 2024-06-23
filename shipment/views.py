from django.shortcuts import render, get_object_or_404, redirect
from .models import Shipment, ShipmentDetail
from Users.models import Users
from .forms import ShipmentDetailForm, ShipmentForm
# Create your views here.

users = Users.objects.all()

def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'html/shipment_list.html', {'shipments': shipments, 'users': users})

def shipment_detail_list(request):
    users = Users.objects.all()
    shipments = Shipment.objects.all()
    shipment_detail = ShipmentDetail.objects.all()
    return render(request, 'html/shipment_detail_list.html', {'shipments': shipments, 'shipment_detail': shipment_detail, 'users': users})

def create_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipment_list')
    else:
        form = ShipmentForm()
    return render(request, 'html/shipment_create.html', {'form': form, 'users': users})

def create_shipment_detail(request):
    if request.method == 'POST':
        form = ShipmentDetailForm(request.POST)
        if form.is_valid():
                shipment_detail = form.save()
                product = shipment_detail.product
                product.product_qty -= shipment_detail.detail_qty
                product.save()
                return redirect('shipment_detail_list')  # or another appropriate view
    else:
        form = ShipmentDetailForm()
    return render(request, 'html/shipment_detail_create.html', {'form': form, 'users': users})


def update_shipment(request, shipment_id):
    shipment = Shipment.objects.get(shipment_id=shipment_id)
    form = ShipmentForm(request.POST or None, instance=shipment)
    if form.is_valid():
        form.save()
        return redirect('shipment_list')
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'html/shipment_update.html', {'form':form, 'users': users})

def update_shipment_detail(request, shipment_id, product_id):
    shipment_detail = get_object_or_404(ShipmentDetail, shipment_id=shipment_id, product_id=product_id)
    origin_qty = shipment_detail.detail_qty

    if request.method == 'POST':
        form = ShipmentDetailForm(request.POST, instance=shipment_detail)
        if form.is_valid():
            update_data = form.save()
            update_qty = update_data.detail_qty - origin_qty
            
            product = shipment_detail.product
            product.product_qty -= update_qty
            product.save()

            return redirect('shipment_detail_list')

    else:
        form = ShipmentDetailForm(instance=shipment_detail)

    return render(request, 'html/shipment_detail_update.html', {'form': form, 'shipment_detail': shipment_detail, 'users': users})

def delete_shipment(request, shipment_id):
    shipment = Shipment.objects.get(shipment_id=shipment_id)
    if request.method == 'POST':
        shipment.delete()
        return redirect('shipment_list')
    return render(request, 'html/shipment_delete.html', {'shipment': shipment, 'users': users})

def delete_shipment_detail(request, shipment_id, product_id):
    shipment_detail = get_object_or_404(ShipmentDetail, shipment_id=shipment_id, product_id=product_id)
    if request.method == 'POST':
        shipment_detail.delete()
        return redirect('shipment_detail_list')
    return render(request, 'html/shipment_detail_delete.html', {'shipment_detail': shipment_detail, 'shipment': shipment_detail.shipment,'detail': shipment_detail, 'users': users})
