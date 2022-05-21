from django.shortcuts import render

from .models import Sandblast, Printing


def sandblast(request):
    sandblasts = Sandblast.sorted_by_size.all()

    context = {
        'sandblasts': sandblasts
    }

    return render(request, 'pages/sandblast.html', context)


def printing(request):
    printings = Printing.sorted_by_size.all()

    context = {
        'printings': printings
    }

    return render(request, 'pages/printing.html', context)
