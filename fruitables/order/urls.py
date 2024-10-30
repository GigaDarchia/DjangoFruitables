from django.urls import path
from .views import CartView, CheckoutView, RemoveFromCart, AddToCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('remove/<int:product_id>/', RemoveFromCart.as_view(), name='remove_from_cart')
]