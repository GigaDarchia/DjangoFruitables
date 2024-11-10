from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Product, Category
from modeltranslation.admin import TranslationAdmin

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'price', 'stock')
    list_editable = ('price', 'stock')
    list_filter = ('category', 'title', 'price')
    search_fields = ('title', 'price')
    fieldsets = [
        (None, {
            'fields': ['title', 'slug', 'category', 'price', 'stock']
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ['description', 'short_desc','img']
        })
    ]
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin, TranslationAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {"slug": ("name",)}