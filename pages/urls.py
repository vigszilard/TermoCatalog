from django.urls import path
from .views import index, AboutPageView, ContactPageView, FAQPageView, send_contact_form

urlpatterns = [
    path('', index, name='index'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('send_contact_form', send_contact_form, name='send_contact_form'),
    path('faq', FAQPageView.as_view(), name='faq')
]