from django.shortcuts import redirect, render, get_object_or_404

from orders.forms import OrderForm, OrderDetailForm
from .models import Order, OrderDetail
from django.db import models

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'html/order_list.html', {'orders': orders})

def order_detail_list(request):
    orders = Order.objects.all()
    order_detail = OrderDetail.objects.all()
    return render(request, 'html/orderdetail_list.html', {'orders': orders, 'order_detail': order_detail})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'html/order_create.html', {'form': form})

def order_detail_create(request):
    if request.method == 'POST':
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_detail_list')
    else:
        form = OrderDetailForm()
    return render(request, 'html/orderdetail_create.html', {'form': form})

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

def order_update_detail(request, order_id, supplier_id, product_id):
    order_detail = get_object_or_404(OrderDetail, order_id=order_id, supplier_id=supplier_id, product_id=product_id)
    if request.method == 'POST':
        form = OrderDetailForm(request.POST, instance=order_detail)
        if form.is_valid():
            form.save()
            return redirect('order_detail_list')
    else:
        form = OrderDetailForm(instance=order_detail)
    return render(request, 'html/orderdetail_update.html', {'form': form, 'order': order_detail})


def order_delete(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'html/order_delete.html', {'order': order})

def order_detail_delete(request, order_id, supplier_id, product_id):
    order_detail = get_object_or_404(OrderDetail, order_id=order_id, supplier_id=supplier_id, product_id=product_id)
    if request.method == 'POST':
        order_detail.delete()
        return redirect('order_detail_list')
    return render(request, 'html/orderdetail_delete.html', {'order_detail': order_detail, 'order': order_detail.order, 'product': order_detail.product})