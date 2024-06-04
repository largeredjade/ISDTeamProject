from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierDetailForm
# Create your views here.

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'html/supplier_list.html', {'suppliers': suppliers})

def create_supplier(request):
    if request.method == 'POST':
        form = SupplierDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
        else:
            form = SupplierDetailForm()
        return render(request, 'html/supplier_create.html',{'form':form})

def update_supplier(request, supplier_id):
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    form = SupplierDetailForm(request.POST or None,instance=supplier)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, 'html/supplier_update.html',{'form':form, 'supplier':supplier})

def delete_supplier(request, supplier_id):
    supplier = Supplier.objects.get(supplier_id=supplier_id)

    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'html/supplier_delete.html',{'supplier':supplier})