from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from shop.models import Product
from .models import Cart, CartItem
from django.views.generic import TemplateView

class CartPage(TemplateView):
    template_name = 'cart.html'

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = Cart.objects.get(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    cart_item.quantity += 1
    cart_item.save()

    # Redirect back to the previous page
    return redirect(request.META.get('HTTP_REFERER', reverse('shop')))

