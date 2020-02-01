from django.shortcuts import render, redirect, reverse
from .models import Product
from .forms import ProductForm
from django.contrib import messages


# Create your views here.

# Show Products
def show_products(request):
    all_products = Product.objects.all()
    return render(request, 'catalog/products.template.html', {
        'all_products':all_products
    })


# Create Product
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product has been created!")
            return redirect(show_products)
      
    else:
        product_form = ProductForm()
  
    return render(request, 'catalog/create_product.template.html', {
        'form': product_form
    })
    