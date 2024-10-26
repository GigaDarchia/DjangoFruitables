from django.urls import path
from .views import add_to_cart, CartPage

urlpatterns = [
    path('', CartPage.as_view(), name='order'),
    path('add/<int:product_id>', add_to_cart, name='add_to_cart'),
]