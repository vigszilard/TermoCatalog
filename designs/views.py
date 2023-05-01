from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Sandblast, Printing


def sandblast(request):
    sandblasts = Sandblast.sorted_by_size.all()
    paginator = Paginator(sandblasts, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'sandblasts': sandblasts,
        'page_obj': page_obj
    }

    return render(request, 'pages/sandblast.html', context)


def printing(request):
    printings = Printing.sorted_by_size.all()
    paginator = Paginator(printings, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'printings': printings,
        'page_obj': page_obj
    }

    return render(request, 'pages/printing.html', context)
