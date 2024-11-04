from .models import Category, Product
from .forms import SearchForm
from django.views.generic import ListView, TemplateView

class HomeView(TemplateView):
    """Simple view for rendering the home page"""
    template_name = 'index.html'


class ProductPageView(TemplateView):
    """Individual product detail page view"""
    template_name = 'shop-detail.html'


class CategoryPageView(ListView):
    """
    Display products filtered by category, including all subcategories
    Uses MPTT (Modified Preorder Tree Traversal) for handling nested categories
    """
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def __init__(self):
        super().__init__()
        self.category = None

    def get_queryset(self):
        # Get category by slug and include all its descendants
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        categories = self.category.get_descendants(include_self=True)
        # Filter products by categories and optimize with select_related
        return Product.objects.filter(category__in=categories).select_related('category')

    def get_context_data(self, **kwargs):
        # Add current category to context for template use
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ProductsView(ListView):
    """Display all products with pagination"""
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        # Optimize query with select_related for category
        return Product.objects.select_related('category')


class SearchView(ListView):
    """
    Handle product search functionality
    Uses a form to get search query and filters products accordingly
    """
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9
    form_class = SearchForm

    def get_queryset(self):
        products = Product.objects.select_related('category')

        # Filter products if search form is valid
        form = self.form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = products.filter(title__icontains=query)

        return products

    def get_context_data(self, **kwargs):
        # Add search form to context, preserving user input if valid
        context = super().get_context_data(**kwargs)
        form = self.form_class(self.request.GET)
        context['form'] = form if form.is_valid() else self.form_class()
        return context


class ProductFilterView(ListView):
    """
    Filter products by price and subcategory
    Maintains filter state in template after submission
    """
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        # Get filter parameters from GET request
        price = self.request.GET.get('price')
        subcategory = self.request.GET.get('subcategory')

        products = Product.objects.select_related('category')

        # Apply filters if parameters exist
        if subcategory and subcategory != 'ყველა':
            products = products.filter(category__name=subcategory)
        if price:
            products = products.filter(price__lte=price)

        return products

    def get_context_data(self, **kwargs):
        # Add selected filter values to context to maintain state
        context = super().get_context_data(**kwargs)
        context['selected_price'] = self.request.GET.get('price', 0)
        context['selected_subcategory'] = self.request.GET.get('subcategory', '')
        return context

class ContactView(TemplateView):
    """Simple view for rendering the contact page"""
    template_name = 'contact.html'

class Error404(TemplateView):
    template_name = '404.html'

class Error500(TemplateView):
    template_name = '500.html'
