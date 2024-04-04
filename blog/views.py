from django.shortcuts import render

from django.http import HttpResponseRedirect

# Create your views here.
from .models import PostModel

from .forms import PostForms


def createPost(request):
    posts = PostModel.objects.all()
    categories = PostModel.objects.values('category').distinct()

    error = None
    form_create = PostForms(request.POST or None)
    if request.method == "POST":

        if form_create.is_valid():

            PostModel.objects.create(
                judul=form_create.cleaned_data.get('judul'),
                isi=form_create.cleaned_data.get('isi'),
                category=form_create.cleaned_data.get('category'),

            )
            return HttpResponseRedirect('/blog/')
        else:

            error = form_create.errors

    context = {
        'page_title': 'Create',
        'title': 'Create',
        'heading': 'Create Page',
        'post': posts,
        'categories': categories,
        'forms_create': form_create,
        'error': error,
    }
    return render(request, 'blog/create.html', context)


def index(request):
    posts = PostModel.objects.all()
    categories = PostModel.objects.values('category').distinct()
    print(categories)
    context = {
        'page_title': 'Blog',
        'title': 'Blog',
        'heading': 'Blog Page',
        'post': posts,
        'categories': categories
    }
    return render(request, 'blog/index.html', context)


def categortyPost(request, categoryInput):
    posts = PostModel.objects.filter(category=categoryInput)
    categories = PostModel.objects.values('category').distinct()
    print(categories)
    context = {
        'page_title': 'Blog',
        'title': 'Blog',
        'heading':  categoryInput,
        'post': posts,
        'categories': categories
    }
    return render(request, 'blog/category.html', context)


def detailPost(request, slugInput):
    posts = PostModel.objects.get(slug=slugInput)
    categories = PostModel.objects.values('category').distinct()
    print(categories)
    context = {
        'page_title': 'Blog',
        'title': 'Blog',
        'heading': 'Blog Page',
        'post': posts,
        'categories': categories
    }
    return render(request, 'blog/detail.html', context)
