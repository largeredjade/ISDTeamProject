from django.shortcuts import render
from shipment.models import Shipment, ShipmentDetail
from deliveries.models import Delivery, DeliveryDetail
from orders.models import Order, OrderDetail
from products.models import Product
from Users.models import Users
from suppliers.models import Supplier

def homepage(request):
    shipments = Shipment.objects.all()
    shipment_details = ShipmentDetail.objects.all()
    deliveries = Delivery.objects.all()
    delivery_details = DeliveryDetail.objects.all()
    orders = Order.objects.all()
    order_details = OrderDetail.objects.all()
    products = Product.objects.all()
    users = Users.objects.all()
    suppliers= Supplier.objects.all()
    return render(request, 'html/homepage.html', {'shipments': shipments, 'shipment_details': shipment_details, 'deliveries': deliveries, 'delivery_details': delivery_details, 'orders': orders, 'order_details': order_details, 'products': products, 'users': users, 'suppliers': suppliers})
