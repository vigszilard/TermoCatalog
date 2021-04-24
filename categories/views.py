from django.shortcuts import render, get_object_or_404

from .models import Category, Gallery

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    gallery = Gallery.objects.filter(category_id=category_id)

    context = {
        'category': category,
        'gallery': gallery
    }

    return render(request, 'pages/category.html', context)
