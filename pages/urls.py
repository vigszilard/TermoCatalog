from django.urls import path
from .views import index, AboutPageView, ContactPageView, faq

urlpatterns = [
    path('', index, name='index'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('faq', faq, name='faq')
]