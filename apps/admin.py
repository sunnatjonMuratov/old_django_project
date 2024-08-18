from django.contrib import admin
from apps.models import Product, Category


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price', 'image',
    search_fields = 'name',
    list_editable = 'price'
    

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

