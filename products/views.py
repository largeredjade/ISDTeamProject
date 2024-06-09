from django.shortcuts import redirect, render
from.models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'html/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # redirect to the product list page
    else:
        form = ProductForm()
    return render(request, 'html/product_create.html', {'form': form})

def product_update(request, product_id):
    #... view logic here...
    return render(request, 'html/product_update.html')

def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')  # redirect to the product list page