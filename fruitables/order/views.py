from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from shop.models import Product
from django.urls import reverse_lazy
from .models import Cart, CartItem
from django.views.generic import TemplateView, ListView, DeleteView
from django.views import View


class CheckoutView(TemplateView):
    """View for rendering the checkout page."""
    template_name = 'checkout.html'


class AddToCartView(LoginRequiredMixin, View):
    """Handles adding a product to the user's cart."""

    login_url = reverse_lazy('login')

    def post(self, request, **kwargs):
        # Get the product by ID or return 404 if not found
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        # Redirect if the product is out of stock
        if product.stock == 0:
            return redirect(request.META.get('HTTP_REFERER'))

        # Retrieve or create the user's cart and cart item
        cart = Cart.objects.get(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        # Increase item quantity in cart and save
        cart_item.quantity += 1
        cart_item.save()

        # Decrease the stock of the product and save
        product.stock -= 1
        product.save()

        # Redirect to the success URL (e.g., shop page)
        return redirect(request.META.get('HTTP_REFERER'))


class CartView(LoginRequiredMixin, ListView):
    """Displays the items in the user's cart."""

    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'items'  # Name used in template to access cart items
    login_url = 'login'

    def get_queryset(self):
        # Retrieve user's cart items, including related product data for optimization
        cart = Cart.objects.get(user=self.request.user)
        items = CartItem.objects.filter(cart=cart).select_related('product')
        return items


class RemoveFromCart(DeleteView):
    """Handles removing an item from the user's cart."""

    model = CartItem
    context_object_name = 'item'  # Name used in template to access the item being removed
    success_url = reverse_lazy('cart')  # Redirect URL after successful deletion

    def get_object(self, queryset=None):
        # Retrieve the CartItem based on user, cart, and product ID
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart = Cart.objects.get(user=self.request.user)
        item = CartItem.objects.get(cart=cart, product=product)
        return item

    def delete(self, request, *args, **kwargs):
        # Handle the product stock update and delete the cart item
        item = self.get_object()
        product = item.product

        # Restore the product stock based on cart item quantity
        product.stock += item.quantity
        product.save()

        # Delete the cart item after stock update
        item.delete()
