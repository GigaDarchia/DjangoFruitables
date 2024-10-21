from django.contrib import admin
from .models import Product, Category, UserCart


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    pass
