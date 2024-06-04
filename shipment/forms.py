from django import forms
from .models import ShipmentDetail

class ShipmentDetailForm(forms.ModelForm):
    class Meta:
        model = ShipmentDetail
        fields = '__all__'