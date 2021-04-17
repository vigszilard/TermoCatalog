from django.contrib import admin

from .models import Category, Gallery

class GalleryInline(admin.TabularInline):
    model = Gallery

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    inlines = [GalleryInline,]

admin.site.register(Category, CategoryAdmin)