from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView

from .models import *


# class GardensView(Category, ListView):
#     model = Gardens
#     # queryset = Gardens.objects.all()
#     template_name = 'main/index.html'


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Gardens.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/index.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def family_class(request):
    return render(request, 'main/family_class.html')


def schedule(request):
    return render(request, 'main/schedule.html')


def contacts(request):
    return render(request, 'main/contacts.html')
