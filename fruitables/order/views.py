from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from shop.models import Product
from .models import Cart, CartItem
from django.views.generic import TemplateView


class CartPage(TemplateView):
    """Simple view for displaying the user's shopping cart"""
    template_name = 'cart.html'


@login_required  # Ensures only logged-in users can add to cart
def add_to_cart(request, product_id):
    # Get the product or return 404 if not found
    product = get_object_or_404(Product, id=product_id)

    # Check if product is in stock before proceeding
    if product.stock <= 0:
        # Redirect back to previous page
        return redirect(request.META.get('HTTP_REFERER'))

    # Get the user's cart
    cart = Cart.objects.get(user=request.user)
    # Get existing cart item or create new one if it doesn't exist
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Increment the quantity of the cart item
    cart_item.quantity += 1
    cart_item.save()

    # Decrease the product stock
    product.stock -= 1
    product.save()

    # Return to the page user came from
    return redirect(request.META.get('HTTP_REFERER'))