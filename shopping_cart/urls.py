from django.urls import path

from .views import add_to_cart, view_cart, remove_from_cart, minus_from_cart

urlpatterns = [
  path('add/<product_id>', add_to_cart, name='add_to_cart'),
  path('', view_cart, name='view_cart'),
  path('minus/<product_id>', minus_from_cart, name='minus_from_cart'),
  path('remove/<product_id>', remove_from_cart, name='remove_from_cart'),
]