from django.contrib import admin
from .models import Product, Sale, Inventory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_16oz', 'stock']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'total', 'timestamp']
    list_filter = ['timestamp', 'product__category']
    search_fields = ['product__name']
    readonly_fields = ['timestamp']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'current_stock', 'last_restock']
    search_fields = ['product__name']
