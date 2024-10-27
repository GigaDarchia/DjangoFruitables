from django.urls import path
from .views import HomeView, SearchView, ProductFilterView, ProductsView, CategoryPageView, ProductPageView, CheckoutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductPageView.as_view(), name="product_page"),
    path('category/filter/', ProductFilterView.as_view(), name='filter_products'),
    path('shop/', ProductsView.as_view(), name='shop'),
    path('order/checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/<slug:slug>/', CategoryPageView.as_view(), name='category_page')
]