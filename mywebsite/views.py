from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'Home',
        'title': 'Home',
        'heading': 'Selamat Datang Di My Website',
    }
    return render(request, 'index.html', context)
