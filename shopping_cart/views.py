from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from catalog.models import Product


# Create your views here.

def add_to_cart(request, product_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    
    # we check if the product_id is not in the cart. If so, we will add it
    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        # product is found, let's add it to the cart
        cart[product_id] = {
            'id':product_id,
            'name': product.name,
            'price': str(product.price),
            'image_url':product.image.cdn_url,
            'quantity':1,
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Product has been added to your cart!")
        return redirect('/shopping_cart/')
        # return render(request, 'catalog/product.template.html')  
        
    else:
        cart[product_id]['quantity']+=1
        request.session['shopping_cart'] = cart
        total_price = round(int(cart[product_id]['quantity']) * float(cart[product_id]['price']),2)
        return render(request, 'cart/view_cart.template.html', {
            'total_price':total_price
        })