from django.urls import path
from .views import add_to_cart, CartPage, CheckoutView

urlpatterns = [
    path('', CartPage.as_view(), name='order'),
    path('add/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]