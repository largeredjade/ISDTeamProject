from django import forms
from .models import Shipment, ShipmentDetail

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = '__all__'
class ShipmentDetailForm(forms.ModelForm):
    class Meta:
        model = ShipmentDetail
        fields = '__all__'

