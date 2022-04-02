from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('mini_garden', mini_garden, name='mini_garden'),
    path('family-class', family_class, name='family_class'),
    path('schedule', schedule, name='schedule'),
    path('contacts', contacts, name='contacts')
]
