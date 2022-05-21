from django.contrib import admin

from .models import Sandblast, Printing


@admin.register(Sandblast)
class SandblastAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_img_preview', 'wide', 'high')
    list_display_links = ('id', 'name')
    list_editable = ('wide', 'high')
    sortable_by = ('id', 'name')
    search_fields = ('name',)
    readonly_fields = ('display_img_preview',)


@admin.register(Printing)
class PrintingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_img_preview', 'wide', 'high')
    list_display_links = ('id', 'name')
    list_editable = ('wide', 'high')
    sortable_by = ('id', 'name')
    search_fields = ('name',)
    readonly_fields = ('display_img_preview',)
