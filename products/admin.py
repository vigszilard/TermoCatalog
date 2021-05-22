from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'display_img_preview')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    sortable_by = ('id', 'name', 'category')
    search_fields = ('name',) 
    readonly_fields = ('display_img_preview',)
