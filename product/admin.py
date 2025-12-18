from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Columns to show in the product list
    list_display = ('id', 'name', 'price', 'stock', 'created_at')
    
    # Filter sidebar by fields
    list_filter = ('created_at', 'price', 'stock')
    
    # Search bar for these fields
    search_fields = ('name', 'description')
    
    # Ordering by newest first
    ordering = ('-created_at',)
    
    # Fields to display in the form
    fields = ('name', 'description', 'price', 'stock')
