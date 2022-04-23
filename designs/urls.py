from django.urls import path

from pages.views import DesignsPageView
from .views import sandblast, printing

urlpatterns = [
    path('', DesignsPageView.as_view(), name='designs'),
    path('sb/', sandblast, name='sandblast'),
    path('pr/', printing, name='printing'),
]