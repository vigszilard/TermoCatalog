from django.urls import path
from .views import index, AboutPageView, contact, faq

urlpatterns = [
    path('', index, name='index'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', contact, name='contact'),
    path('faq', faq, name='faq')
]