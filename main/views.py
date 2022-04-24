from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView

from .models import *


class ScheduleType:
    def get_schedule(self):
        return Category.objects.all()


class GardensView(Category, ListView):
    model = Gardens
    # queryset = Gardens.objects.all()
    template_name = 'main/index.html'




#
# def mini_garden(request):
#     return render(request, 'main/mini_garden.html')


def family_class(request):
    return render(request, 'main/family_class.html')


def schedule(request):
    return render(request, 'main/schedule.html')


def contacts(request):
    return render(request, 'main/contacts.html')
