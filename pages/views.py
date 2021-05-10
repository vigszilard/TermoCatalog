from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.views.generic import TemplateView
from django.template import loader
from pages.models import AboutPage, ContactPage, FAQPage, Partner
from categories.models import Category 
from smtplib import SMTPException


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
        context['partners'] = Partner.objects.all()
        return context


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of first contactPage template
        context['contact_page'] = ContactPage.objects.first()
        return context

def send_contact_form(request):
    if request.method == 'POST':
        subject = "Termototal contact"
        body = {
            'name' : request.POST['name'],
            'email' : request.POST['email'],
            'phone' : request.POST['phone'],
            'message' : request.POST['message'],
        }
        html_message = loader.render_to_string(
            'components/_email_template.html',
            {
                'name': body['name'],
                'email':  body['email'],
                'phone': body['phone'],
                'message': body['message'] 
            }
        )
        message = '\n'.join(body.values())
        try:
            send_mail(subject, message, 'svc@termototal.ro', ['proiectare@termototal.ro'], fail_silently=False, html_message=html_message)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except SMTPException as ex:
            messages.error(request, 'Solicitarea dvs. nu a putut fi trimisă. Vă rugăm să reîncercați.')
            print("The email could not be sent", ex)
            return redirect("contact")
        messages.success(request, 'Solicitarea dvs. a fost trimisă cu succes.')
        return redirect("contact")
    return render(request, "pages/contact.html")

class FAQPageView(TemplateView):
    template_name = 'pages/faq.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of FAQ template
        context['faqs'] = FAQPage.objects.all()
        return context