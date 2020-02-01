from django.shortcuts import render
from .models import Product, Category

# Create your views here.

# Show Products
def show_products(request):
    all_products = Product.objects.all()
    return render(request, 'catalog/products.template.html', {
        'all_products':all_products
    })
