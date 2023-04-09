from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'category', 'display_img_preview')
    list_display_links = ('id', )
    list_filter = ('category',)
    sortable_by = ('id', 'name', 'number', 'category')
    search_fields = ('name',) 
    readonly_fields = ('display_img_preview',)
    list_editable = ('name', 'number', )
