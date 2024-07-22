from django.contrib import admin
from apps.models import Product, Category


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price', 'image',
    search_fields = 'name',
    list_editable = 'price',

    # def __init__(self, model, admin_site):
    #     super().__init__(model, admin_site)
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

