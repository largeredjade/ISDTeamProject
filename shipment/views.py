from django.shortcuts import render, get_object_or_404, redirect
from .models import Shipment, ShipmentDetail
from .forms import ShipmentDetailForm
# Create your views here.

def shipment_list(request):
    shipments = Shipment.objects.all()
    shipment_detail = ShipmentDetail.objects.all()
    return render(request, 'html/shipment_list.html', {'shipments': shipments, 'shipment_detail': shipment_detail})

def create_shipment_detail(request):
    if request.method == 'POST':
        form = ShipmentDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipment_list')  # or another appropriate view
    else:
        form = ShipmentDetailForm()
    return render(request, 'html/shipment_create.html', {'form': form})


def update_shipment_detail(request, shipment_id, product_id):
    # shipment_id와 product_id를 사용하여 ShipmentDetail을 가져옴
    shipment_detail = get_object_or_404(ShipmentDetail, shipment_id=shipment_id, product_id=product_id)

    if request.method == 'POST':
        form = ShipmentDetailForm(request.POST, instance=shipment_detail)
        if form.is_valid():
            form.save()
            return redirect('shipment_detail', shipment_id=shipment_id)
    else:
        form = ShipmentDetailForm(instance=shipment_detail)

    return render(request, 'html/shipment_update.html', {'form': form})

def delete_shipment_detail(request, shipment_id, product_id):
    shipment_detail = get_object_or_404(ShipmentDetail, shipment_id=shipment_id, product_id=product_id)
    if request.method == 'POST':
        shipment_detail.delete()
        return redirect('shipment_detail_list')
    return render(request, 'html/shipment_delete.html', {'shipment_detail': shipment_detail})
