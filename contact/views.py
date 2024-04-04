from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import ContactForm

from .models import ContactModel


def index(request):
    data_contact = ContactModel.objects.all()
    print(data_contact)

    context = {
        'page_title': 'Contact',
        'title': 'Contact',
        'heading': 'Silahkan isi Contact Anda',
        'contact': data_contact,
    }

    return render(request, 'contact/index.html', context)


def create(request):
    forms = ContactForm()

    if request.method == "POST":
        ContactModel.objects.create(
            nama=request.POST.get('nama'),
            email=request.POST.get('email'),
            alamat=request.POST.get('nama'),
        )
        return HttpResponseRedirect('/contact/')

    context = {
        'page_title': 'Create',
        'title': 'Create File',
        'heading': 'Silahkan isi Contact Anda',
        'form_contact': forms
    }

    return render(request, 'contact/create.html', context)
