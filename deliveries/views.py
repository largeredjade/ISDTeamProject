from django.shortcuts import render, get_object_or_404, redirect
from .models import Delivery, DeliveryDetail
from orders.models import OrderDetail
from Users.models import Users
from .forms import DeliveryForm, DeliveryDetailForm
# Create your views here.

users = Users.objects.all()

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'html/delivery_list.html', {'deliveries': deliveries, 'users': users})

def delivery_detail_list(request):
    deliveries = Delivery.objects.all()
    delivery_detail = DeliveryDetail.objects.all()
    return render(request, 'html/delivery_detail_list.html', {'deliveries': deliveries, 'delivery_detail': delivery_detail, 'users': users})

def create_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else:
        form = DeliveryForm()
    return render(request, 'html/delivery_create.html', {'form': form, 'users': users})

def create_delivery_detail(request):
    if request.method == 'POST':
        form = DeliveryDetailForm(request.POST)
        if form.is_valid():
            delivery_detail = form.save(commit=False)
            product = delivery_detail.product

            try:
                order_detail = OrderDetail.objects.get(order=delivery_detail.order, product=product)
                max_order_qty = order_detail.detail_qty

                if delivery_detail.detail_qty > max_order_qty:
                    form.add_error('detail_qty', f'최대 주문량 {max_order_qty}을 넘었습니다.')
                else:
                    product.product_qty += delivery_detail.detail_qty
                    product.save()
                    delivery_detail.save()
                    return redirect('delivery_detail_list')
            except OrderDetail.DoesNotExist:
                form.add_error('product', f'주문내역에 포함되지 않은 상품 {product}입니다')

    else:
        form = DeliveryDetailForm()
    return render(request, 'html/delivery_detail_create.html', {'form': form, 'users': users})


def update_delivery(request, delivery_id):
    delivery = Delivery.objects.get(delivery_id = delivery_id)
    form = DeliveryForm(request.POST or None, instance=delivery)
    if form.is_valid():
        form.save()
        return redirect('delivery_list')
    else:
        form = DeliveryForm(instance=delivery)
    return render(request, 'html/delivery_update.html', {'form':form, 'users': users})

def update_delivery_detail(request, delivery_id, product_id, order_id, user_id):
    delivery_detail = get_object_or_404(DeliveryDetail, delivery_id=delivery_id, product_id=product_id, order_id=order_id, user_id=user_id)
    origin_qty = delivery_detail.detail_qty
    if request.method == 'POST':
        form = DeliveryDetailForm(request.POST, instance=delivery_detail)
        if form.is_valid():
            update_data = form.save()
            update_qty = update_data.detail_qty - origin_qty
            
            product = delivery_detail.product
            product.product_qty += update_qty
            product.save()
            return redirect('delivery_detail_list')
    else:
        form = DeliveryDetailForm(instance=delivery_detail)

    return render(request, 'html/delivery_detail_update.html', {'form': form, 'delivery_detail': delivery_detail, 'users': users})

def delete_delivery(request, delivery_id):
    delivery = Delivery.objects.get(delivery_id = delivery_id)
    if request.method == 'POST':
        delivery.delete()
        return redirect('delivery_list')
    return render(request, 'html/delivery_delete.html', {'delivery': delivery, 'users': users})


def delete_delivery_detail(request, delivery_id, product_id, order_id, user_id):
    delivery_detail = get_object_or_404(DeliveryDetail, delivery_id=delivery_id, product_id=product_id,
                                        order_id=order_id, user_id=user_id)

    if request.method == 'POST':
        delivery_detail.delete()
        return redirect('delivery_detail_list')

    return render(request, 'html/delivery_detail_delete.html', {'delivery_detail': delivery_detail, 'users': users})