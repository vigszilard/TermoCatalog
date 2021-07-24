from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from smtplib import SMTPException
from .models import Product


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'pages/product.html', context)


def send_offer_form(request):
    if request.method == 'POST':
        subject = "Termototal cerere oferta"
        # file = request.FILES['file']
        body = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'transport': request.POST.get('transport', '') == 'on',
            'montage': request.POST.get('montage', '') == 'on',
            'city': request.POST['city'],
            'message': request.POST['message'],
            'product_id': request.POST['product']
        }
        product = get_object_or_404(Product, pk=body['product_id'])
        html_message = loader.render_to_string(
            'request_offer_email.html',
            {
                'name': body['name'],
                'email':  body['email'],
                'phone': body['phone'],
                'transport': body['transport'],
                'montage': body['montage'],
                'city': body['city'],
                'message': body['message'],
                'product_name': product.name,
                'product_img': product.display_img
            }
        )
        message = '\n'.join(str(body.values()))
        try:
            send_mail(subject, message, 'svc@termototal.ro',
                      ['rafigeorgescu@gmail.com'], fail_silently=False, html_message=html_message)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except SMTPException as ex:
            messages.error(
                request, 'Solicitarea dvs. nu a putut fi trimisă. Vă rugăm să reîncercați.')
            print("The email could not be sent", ex)
            return redirect("contact")
        messages.success(request, 'Solicitarea dvs. a fost trimisă cu succes.')
        return redirect("product", body['product_id'])
    return render(request, "pages/product.html")
