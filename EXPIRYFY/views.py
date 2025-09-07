from django.shortcuts import render

def home(request):
    return render(request, 'efy/index.html')


def dashboard(request):
    return render(request, 'efy/home.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Add Product
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("view")
    else:
        form = ProductForm()
    return render(request, "efy/add_product.html", {"form": form})

# Update Product
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("view_product")
    else:
        form = ProductForm(instance=product)
    return render(request, "efy/update_product.html", {"form": form, "product": product})

# Delete Product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("view_product")
    return render(request, "efy/delete_product.html", {"product": product})

# View Products by Rack No
def view_product(request):
    query = request.GET.get("rack_no")
    products = None
    if query:
        products = Product.objects.filter(rack_no=query)
    return render(request, "efy/view_product.html", {"products": products})

