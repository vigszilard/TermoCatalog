from django.contrib import admin
from .models import AboutPage, ContactPage, FAQPage

class FAQPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')

admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.register(FAQPage, FAQPageAdmin)