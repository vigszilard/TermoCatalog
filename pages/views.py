from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from pages.models import AboutPage, ContactPage

from categories.models import Category 


def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'pages/index.html', context)


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of first aboutPage template
        context['about_page'] = AboutPage.objects.first()
        return context


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of first contactPage template
        context['contact_page'] = ContactPage.objects.first()
        return context


def faq(request):
    return render(request, 'pages/faq.html')

