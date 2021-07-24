from django.urls import path

from . import views

urlpatterns = [
    path('<int:product_id>', views.product, name='product'),
    path('request_offer', views.send_offer_form, name='request_offer'),
]