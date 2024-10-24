from django.urls import path
from .views import home, product_page, products, cart, contact, checkout, search, category_page

urlpatterns = [

    path('', home, name='home'),
    path('product/', product_page, name="product_page"),
    path('category/', products, name='shop'),
    path('order/cart/', cart, name='cart'),
    path('order/checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('category/<slug:slug>/', category_page, name='category_page')

]