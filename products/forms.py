from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_sellingprice', 'product_volume', 'product_weight', 'product_location', 'maintenance_cost', 'product_qty', 'product_minQty')