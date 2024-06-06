from django.shortcuts import render, get_object_or_404, redirect
from .models import Delivery, DeliveryDetail
from .forms import DeliveryForm, DeliveryDetailForm
# Create your views here.

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'html/delivery_list.html', {'deliveries': deliveries})

def delivery_detail_list(request):
    deliveries = Delivery.objects.all()
    delivery_detail = DeliveryDetail.objects.all()
    return render(request, 'html/delivery_detail_list.html', {'deliveries': deliveries, 'delivery_detail': delivery_detail})

def create_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else:
        form = DeliveryForm()
    return render(request, 'html/delivery_create.html', {'form': form})

def create_delivery_detail(request):
    if request.method == 'POST':
        form = DeliveryDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery_detail_list')  # or another appropriate view
    else:
        form = DeliveryDetailForm()
    return render(request, 'html/delivery_detail_create.html', {'form': form})


def update_delivery(request, delivery_id):
    delivery = Delivery.objects.get(delivery_id = delivery_id)
    form = DeliveryForm(request.POST or None, instance=delivery)
    if form.is_valid():
        form.save()
        return redirect('delivery_list')
    else:
        form = DeliveryForm(instance=delivery)
    return render(request, 'html/delivery_update.html', {'form':form})
def update_delivery_detail(request, delivery_id, product_id, order_id, user_id):
    delivery_detail = get_object_or_404(DeliveryDetail, delivery_id=delivery_id, product_id=product_id, order_id=order_id, user_id=user_id)

    if request.method == 'POST':
        form = DeliveryDetailForm(request.POST, instance=delivery_detail)
        if form.is_valid():
            form.save()
            return redirect('delivery_detail_list')
    else:
        form = DeliveryDetailForm(instance=delivery_detail)

    return render(request, 'html/delivery_detail_update.html', {'form': form, 'delivery_detail': delivery_detail})

def delete_delivery(request, delivery_id):
    delivery = Delivery.objects.get(delivery_id = delivery_id)
    if request.method == 'POST':
        delivery.delete()
        return redirect('delivery_list')
    return render(request, 'html/delivery_delete.html', {'delivery': delivery})


def delete_delivery_detail(request, delivery_id, product_id, order_id, user_id):
    delivery_detail = get_object_or_404(DeliveryDetail, delivery_id=delivery_id, product_id=product_id,
                                        order_id=order_id, user_id=user_id)

    if request.method == 'POST':
        delivery_detail.delete()
        return redirect('delivery_detail_list')

    return render(request, 'html/delivery_detail_delete.html', {'delivery_detail': delivery_detail})