from django.urls import path

from . import views

urlpatterns = [
    path('<int:category_id>', views.category, name='category'),
]