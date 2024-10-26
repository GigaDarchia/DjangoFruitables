from django.urls import path
from .views import HomeView, contact, checkout, search, filter_products, ProductsView, CategoryPageView, ProductPageView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductPageView.as_view(), name="product_page"),
    path('category/filter/', filter_products, name='filter_products'),
    path('shop/', ProductsView.as_view(), name='shop'),
    path('order/checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('category/<slug:slug>/', CategoryPageView.as_view(), name='category_page')
]