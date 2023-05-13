from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from vetsite.forms import ContactForm
from vetsite.models import *


def index(request):
    categories = Category.objects.all()[:3]
    form = ContactForm
    return render(request, 'VetCat/index.html', {'categories': categories, 'form': form})


def catalog(request):
    categories = Category.objects.all()
    return render(request, 'VetCat/catalog.html', {'categories': categories})


def services(request, pk):
    category = get_object_or_404(Category, pk=pk)
    services = Services.objects.filter(category=category)
    context = {'category': category, 'services': services}
    return render(request, 'VetCat/services.html', context)


def about(request):
    return render(request, 'VetCat/about.html')


def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка отправки сообщения')

            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'VetCat/contact.html', context)


class DoctorListView(generic.ListView):
    model = Doctors
    template_name = 'VetCat/doctor.html'
    context_object_name = 'doctor_list'


class DoctorDetailView(generic.DetailView):
    model = Doctors
    template_name = 'VetCat/doctor_detail.html'
