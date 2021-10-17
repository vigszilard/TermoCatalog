from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from smtplib import SMTPException
from .models import Product
from django.conf import settings
import os


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'pages/product.html', context)


def send_offer_form(request):
    if request.method == 'POST':
        subject = "Termototal cerere oferta"
        body = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'transport': request.POST.get('transport', '') == 'on',
            'assembly': request.POST.get('assembly', '') == 'on',
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
                'assembly': body['assembly'],
                'city': body['city'],
                'message': body['message'],
                'product_name': product.name,
                'product_img': product.display_img
            }
        )
        message = '\n'.join(str(body.values()))
        attachment = None
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email='svc@termototal.ro',
            to=['proiectare@termototal.ro']
        )
        email.attach_alternative(html_message, "text/html")
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            if str(uploaded_file.content_type) == 'image/jpeg' or str(uploaded_file.content_type) == 'image/png':
                if int(uploaded_file.size) <= 5000000:
                    fs = FileSystemStorage()
                    attachment = fs.save('attachments/' + uploaded_file.name, uploaded_file)
                    email.attach_file(os.path.join(settings.MEDIA_ROOT + '/' + attachment))
                else:
                    messages.error(request, 'Fișierul atașat are o dimensiune prea mare.')
                    return redirect("product", body['product_id'])
            else:
                messages.error(request, 'Fișierul atașat nu este acceptat.')
                return redirect("product", body['product_id'])
        get_recaptcha = request.POST.get("g-recaptcha-response")
        if get_recaptcha:
            try:
                email.send(fail_silently=False)
                if attachment is not None:
                    os.remove(os.path.join(settings.MEDIA_ROOT + '/' + attachment))

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except SMTPException:
                messages.error(request, 'Solicitarea dvs. nu a putut fi trimisă. Vă rugăm să reîncercați.')
                return redirect("product", body['product_id'])
            messages.success(request, 'Solicitarea dvs. a fost trimisă cu succes.')
            return redirect("product", body['product_id'])
        else:
                messages.error(request, 'Vă rugăm să completați reCaptcha.')
                return redirect("product", body['product_id'])
    return render(request, "pages/product.html")
