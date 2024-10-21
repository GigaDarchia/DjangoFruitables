from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def product_page(request):
    return render(request, 'shop-detail.html')

def products(request):
    return render(request, 'shop.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')


