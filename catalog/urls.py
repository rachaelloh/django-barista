from django.urls import path
from .views import show_products, create_product, update_product


urlpatterns = [
    path('', show_products, name='show_products'),
    path('create', create_product),
    path('update/<product_id>', update_product, name='update_product'),
]