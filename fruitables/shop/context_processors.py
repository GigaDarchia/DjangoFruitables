from .models import Category

def category_processor(request):
    return {'categories': Category.objects.filter(parent=None), 'subcategories': Category.objects.filter(parent__isnull=False)}