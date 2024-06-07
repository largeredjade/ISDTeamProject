from django.shortcuts import render, redirect
from .models import Supplier
from Users.models import Users
from .forms import SupplierDetailForm
# Create your views here.

users = Users.objects.all()

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'html/supplier_list.html', {'suppliers': suppliers, 'users': users})

def create_supplier(request):
    if request.method == 'POST':
        form = SupplierDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierDetailForm()
    return render(request, 'html/supplier_create.html', {'form': form, 'users': users})

def update_supplier(request, supplier_id):
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    form = SupplierDetailForm(request.POST or None, instance=supplier)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    else:
        form = SupplierDetailForm(instance=supplier)
    return render(request, 'html/supplier_update.html',{'form': form, 'users': users})

def delete_supplier(request, supplier_id):
    supplier = Supplier.objects.get(supplier_id=supplier_id)

    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'html/supplier_delete.html', {'supplier':supplier, 'users': users})