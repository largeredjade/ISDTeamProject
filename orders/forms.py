from django import forms
from .models import Order, OrderDetail

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_id', 'order_date', 'order_status','user','order_totalcost','expected_arrivaldate')  # specify the fields to include in the form

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'