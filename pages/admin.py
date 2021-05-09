from django.contrib import admin
from .models import AboutPage, ContactPage, FAQPage, Partner

class FAQPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')

admin.site.register(AboutPage)
admin.site.register(Partner)
admin.site.register(ContactPage)
admin.site.register(FAQPage, FAQPageAdmin)