from django.contrib import admin

from .models import Category, Gallery

class GalleryInline(admin.TabularInline):
    model = Gallery

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_img_preview', 'relevance')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'relevance')
    list_editable = ('relevance', )
    search_fields = ('name',)
    inlines = [GalleryInline,]
    readonly_fields = ('display_img_preview',)