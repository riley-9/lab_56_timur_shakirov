from django.contrib import admin

from webapp.models import Product


class ProductsListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'image', 'category', 'rest', 'price']
    list_filter = ['id', 'title', 'description', 'image', 'category', 'rest', 'price']
    search_fields = ['title', 'category']
    fields = ['id', 'title', 'description', 'image', 'category', 'rest', 'price']
    readonly_fields = ['id']


admin.site.register(Product, ProductsListAdmin)
