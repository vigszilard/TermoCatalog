from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import AboutPage, ContactPage, DesignsPage, FAQPage, Partner


@admin.register(FAQPage)
class FAQPageAdmin(ModelAdmin):
    list_display = ('id', 'question', 'answer')


@admin.register(AboutPage)
class AboutPageAdmin(ModelAdmin):
    pass


@admin.register(Partner)
class PartnerAdmin(ModelAdmin):
    list_display = ('id', 'name')


@admin.register(ContactPage)
class ContactPageAdmin(ModelAdmin):
    pass


@admin.register(DesignsPage)
class DesignsPageAdmin(ModelAdmin):
    pass
