from django.shortcuts import render

def home(request):
    return render(request, 'efy/index.html')



from django.shortcuts import render
from .models import Rack

def dashboard(request):
    racks = Rack.objects.all().order_by('rack_no')  # All racks ordered
    context = {
        "racks": racks,
        "total_racks": racks.count(),
        "total_products":  Product.objects.count(),
        "total_users": 10,  # replace with your User model count
        "total_employees": 5,  # replace with your Employee model count
    }
    return render(request, "efy/home.html", context)











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

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

# Billing page
def billing_page(request):
    return render(request, "efy/billing.html")

# Fetch product by batch number
def get_product_by_batch(request):
    batch_no = request.GET.get("batch_no")
    try:
        product = Product.objects.get(batch_no=batch_no)
        data = {
            "id": product.id,
            "rack_no": product.rack_no,
            "batch_no": product.batch_no,
            "name": product.product_name,
            "image": product.image.url if product.image else "",  # ✅ FIXED
            "price": float(product.price),
            "stock": product.quantity,
            "expiry_date": product.expiry_date.strftime("%Y-%m-%d"),
        }
        return JsonResponse({"success": True, "product": data})
    except Product.DoesNotExist:
        return JsonResponse({"success": False, "error": "❌ Product not found"})

# Checkout → reduce stock
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt   # ❌ only use if you're testing, better to send CSRF token
def checkout(request):
    if request.method == "POST":
        try:
            cart_data = json.loads(request.body)  # expecting JSON from JS
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON data"})

        updated_items = []
        errors = []

        for item in cart_data:
            try:
                product = Product.objects.get(id=item["id"])
                qty = int(item["qty"])

                if product.quantity >= qty:
                    product.quantity -= qty
                    product.save()

                    updated_items.append({
                        "id": product.id,
                        "name": product.product_name,
                        "remaining_stock": product.quantity,
                    })
                else:
                    errors.append({
                        "id": product.id,
                        "name": product.product_name,
                        "error": f"Not enough stock (Available: {product.quantity})"
                    })
            except Product.DoesNotExist:
                errors.append({"id": item["id"], "error": "Product not found"})

        if errors:
            return JsonResponse({"success": False, "message": "Some items failed", "errors": errors})

        return JsonResponse({"success": True, "message": "✅ Bill saved & stock updated", "updated": updated_items})

    return JsonResponse({"success": False, "message": "Invalid request method"})


