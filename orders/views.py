from django.shortcuts import redirect, render, get_object_or_404

from orders.forms import OrderForm
from .models import Order, OrderDetail
from django.db import models

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'html/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_details = OrderDetail.objects.filter(order=order)
    return render(request, 'html/order_detail.html', {'order': order, 'order_details': order_details})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('html/order_list.html')
    else:
        form = OrderForm()
    return render(request, 'html/order_create.html', {'form': form})


def order_update(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'html/order_update.html', {'form': form, 'order': order})

def order_delete(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect('order_list')