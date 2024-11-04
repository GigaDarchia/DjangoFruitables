from django.urls import path
from django.conf.urls import handler404
from .views import HomeView, SearchView, ProductFilterView, ProductsView, CategoryPageView, ProductPageView, \
    ContactView, Error404, Error500
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductPageView.as_view(), name="product_page"),
    path('shop/filter/', ProductFilterView.as_view(), name='filter_products'),
    path('shop/', vary_on_cookie(cache_page(60*15)(ProductsView.as_view())), name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/<slug:slug>/', vary_on_cookie(cache_page(60*15)(CategoryPageView.as_view())), name='category_page'),
]

