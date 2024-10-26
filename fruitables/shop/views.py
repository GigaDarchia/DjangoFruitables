from django.shortcuts import render
from .models import Category, Product
from django.core.paginator import Paginator
from .forms import SearchForm
from django.views.generic import ListView, DetailView, TemplateView


def paginator_helper(request, queryset):
    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def home(request):
    return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = 'index.html'

class ProductPageView(TemplateView):
    template_name = 'shop-detail.html'

class CategoryPageView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        categories = category.get_descendants(include_self=True)

        return Product.objects.filter(category__in=categories).select_related('category').order_by('title')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

class ProductsView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.select_related('category').all()


def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        products = Product.objects.filter(title__icontains=query)
        page_obj = paginator_helper(request, products)

        return render(request, 'shop.html', context={'products': page_obj, 'form': form})
    else:
        return render(request, 'shop.html', context={'form': SearchForm()})

def filter_products(request):
    price = request.GET.get('price')
    subcategory = request.GET.get('subcategory')

    product_list = Product.objects.select_related('category').all()

    if subcategory:
        product_list = product_list.filter(category__name=subcategory).select_related('category').all()
    if price:
        product_list = product_list.filter(price__lte=price).select_related('category').all()

    page_obj = paginator_helper(request, product_list)

    return render(request, 'shop.html', context={'products': page_obj})


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')

def test(request):
    pass