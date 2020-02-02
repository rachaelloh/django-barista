from django.urls import path
from .views import show_products, create_product, update_product, confirm_delete_product, actually_delete_product


urlpatterns = [
    path('', show_products, name='show_products'),
    path('create', create_product),
    path('update/<product_id>', update_product, name='update_product'),
    path('confirm_delete/<product_id>', confirm_delete_product),
    path('actually_delete/<product_id>', actually_delete_product, name='delete_product'),
]