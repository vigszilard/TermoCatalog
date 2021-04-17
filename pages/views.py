from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from pages.models import AboutPage


def index(request):
    return render(request, 'pages/index.html')


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of first aboutPage template
        context['about_page'] = AboutPage.objects.first()
        return context


def contact(request):
    return render(request, 'pages/contact.html')


def faq(request):
    return render(request, 'pages/faq.html')

