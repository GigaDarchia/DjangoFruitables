from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock')
    list_editable = ('price', 'stock')
    list_filter = ('category', 'title', 'price')
    search_fields = ('title', 'price')
    fieldsets = [
        (None, {
            'fields': ['title', 'category', 'price', 'stock']
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ['description', 'short_desc', 'slug', 'img']
        })
    ]

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'slug', 'parent')
