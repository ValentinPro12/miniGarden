from django.urls import path
from .views import *
from . import views


urlpatterns = [
    # path('', index, name='index'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    # path('mini_garden', mini_garden, name='mini_garden'),
    path('family-class', family_class, name='family_class'),
    path('schedule', schedule, name='schedule'),
    path('contacts', contacts, name='contacts')
]
