from django.shortcuts import render
from .models import Category, Product
from django.core.paginator import Paginator
from .forms import SearchForm

def home(request):
    return render(request, 'index.html')

def product_page(request):
    return render(request, 'shop-detail.html')

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    categories = category.get_descendants(include_self=True)
    product_list = Product.objects.filter(category__in=categories).select_related('category')

    return render(request, 'shop.html', context={'products': product_list,
                                                 'category': category,
                                                 })
def products(request):
    product_list = Product.objects.select_related('category').all()
    paginator = Paginator(product_list, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop.html', context={'products': page_obj})

def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        products = Product.objects.filter(title__icontains=query)
        print(query)
        return render(request, 'shop.html', context={'products': products, 'form': form, 'query': query})
    else:
        return render(request, 'shop.html', context={'form': SearchForm()})

def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')

def test(request):
    pass