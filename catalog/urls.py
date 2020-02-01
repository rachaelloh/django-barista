from django.urls import path
from .views import show_products, create_product


urlpatterns = [
    path('', show_products, name='show_products'),
    path('create', create_product),
]