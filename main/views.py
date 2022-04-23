from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import *


class Grup:
    def get_grup(self):
        return Schedule.objects.all()


class GardensView(Grup, View):
    def get(self, request):
        gardens = Gardens.objects.all()
        lessons = Lessons.objects.all()
        return render(request, 'main/index.html', {'gardens': gardens, 'lessons': lessons})


# def index(request):
#     gardens = Gardens.objects.all()
#     contex = {'gardens': gardens}
#     return render(request, 'main/index.html', contex)


def mini_garden(request):
    return render(request, 'main/mini_garden.html')


def family_class(request):
    return render(request, 'main/family_class.html')


def schedule(request):
    return render(request, 'main/schedule.html')


def contacts(request):
    return render(request, 'main/contacts.html')
