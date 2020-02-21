from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from catalog.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def add_to_cart(request, product_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    
    # we check if the game_id is not in the cart. If so, we will add it
    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        # game is found, let's add it to the cart
        cart[product_id] = {
            'id':product_id,
            'name': product.name,
            'price': str(product.price),
            'image_url':product.image.cdn_url,
            'quantity':1,
            'total_price':float(product.price)
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Game has been added to your cart")
        return redirect('/shopping_cart/')
        
    # elif game_id in cart:    
        # if press again
        # messages.success(request, "The game is already in your shopping cart")
        # return redirect('/cart/')
        
    else:
        
        cart[product_id]['quantity']+=1
        cart[product_id]['total_price'] = round(int(cart[product_id]['quantity']) * float(cart[product_id]['price']),2)
        request.session['shopping_cart'] = cart
        return redirect('/shopping_cart/')        

        
        
def minus_from_cart(request, product_id):
    cart = request.session.get('shopping_cart', {})
    if product_id in cart:
        product = get_object_or_404(Product, pk=product_id) 
        if cart[product_id]['quantity'] > 1:
            cart[product_id]['quantity']-=1
            cart[product_id]['total_price'] = round(int(cart[product_id]['quantity']) * float(cart[product_id]['price']),2)
        # save the cart back to sessions
            request.session['shopping_cart'] = cart
        return redirect('/shopping_cart/')          
        
    
def total_price(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('shopping_cart', {})
    cart[product_id] = {
    'id':product_id,
    'name': product.name,
    'price': str(product.price),
    'image_url':product.image.cdn_url,
    'quantity':cart['quantity'],
    'total_price':round(int(cart[product_id]['quantity']) * float(cart[product_id]['price']),2)
    }
    request.session['shopping_cart'] = cart
    print(cart[product_id]['quantity'])        
    return render(request, 'shopping_cart/view_cart.template.html', {
            'total_price':total_price
        })        
     
    
        
def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    overall_total_price = 0.00
    for id, product in cart.items():
        overall_total_price += product['total_price']
    
    return render(request, 'shopping_cart/view_cart.template.html', {
        'shopping_cart':cart,
        'overall_total_price': round(overall_total_price, 2)
    })
    
    
    
def remove_from_cart(request, product_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the product is in the cart
    if product_id in cart:
        # remove it from the cart
        del cart[product_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")
        
    return redirect(view_cart)