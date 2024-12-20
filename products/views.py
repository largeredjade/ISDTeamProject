from django.shortcuts import get_object_or_404, redirect, render
from.models import Product
from .forms import ProductForm

def product_id(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'html/product_id.html', {'product': product})

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
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'html/product_update.html', {'form': form, 'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Check if the request method is POST
    if request.method == 'POST':
        # If POST, it means the user confirmed the deletion, so delete the product
        product.delete()
        # Redirect to the product list page
        return redirect('product_list')

    # If the request method is not POST, render the confirmation template
    return render(request, 'html/product_delete.html', {'product': product})
