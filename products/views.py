from django.shortcuts import render, get_object_or_404
from .models import Product


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'pages/product.html', context)
