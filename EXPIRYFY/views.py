from django.shortcuts import render

def home(request):
    return render(request, 'efy/index.html')


def dashboard(request):
    return render(request, 'efy/home.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# Add Product
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "efy/add_product.html", {"form": form})

# Update Product
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "efy/update_product.html", {"form": form, "product": product})

# Delete Product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect("product_list")
    return render(request, "efy/delete_product.html", {"product": product})

# Product List
def product_list(request):
    products = Product.objects.all()
    return render(request, "efy/product_list.html", {"products": products})

# View product by rack_no
def view_by_rack(request):
    product = None
    if request.method == "POST":
        rack_no = request.POST.get("rack_no")
        try:
            product = Product.objects.get(rack_no=rack_no)
        except Product.DoesNotExist:
            messages.error(request, "No product found for this rack number.")
    return render(request, "efy/view_by_rack.html", {"product": product})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Rack
from .forms import RackForm

# Add Rack
def rack_add(request):
    if request.method == 'POST':
        form = RackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rack_view')
    else:
        form = RackForm()
    return render(request, 'efy/rack_add.html', {'form': form})

# Update Rack
def rack_update(request, pk):
    rack = get_object_or_404(Rack, pk=pk)
    if request.method == 'POST':
        form = RackForm(request.POST, request.FILES, instance=rack)
        if form.is_valid():
            form.save()
            return redirect('rack_view')
    else:
        form = RackForm(instance=rack)
    return render(request, 'efy/rack_update.html', {'form': form})

# Delete Rack
def rack_delete(request, pk):
    rack = get_object_or_404(Rack, pk=pk)
    if request.method == 'POST':
        rack.delete()
        return redirect('rack_view')
    return render(request, 'efy/rack_delete.html', {'rack': rack})

# View Rack
def rack_view(request):
    racks = Rack.objects.all()
    return render(request, 'efy/rack_view.html', {'racks': racks})


