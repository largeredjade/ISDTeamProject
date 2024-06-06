from django import forms
from .models import Delivery, DeliveryDetail

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

class DeliveryDetailForm(forms.ModelForm):
    class Meta:
        model = DeliveryDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DeliveryDetailForm, self).__init__(*args, **kwargs)
        self.fields['delivery'].widget.attrs['readonly'] = True
        self.fields['product'].widget.attrs['readonly'] = True
        self.fields['order'].widget.attrs['readonly'] = True
        self.fields['user'].widget.attrs['readonly'] = True