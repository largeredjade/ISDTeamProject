from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_id', 'order_date', 'order_status','user_id','order_totalcost','expected_arrivaldate')  # specify the fields to include in the form