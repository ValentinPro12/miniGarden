from django.contrib import admin
from .models import *


# Register your models here.

class GardensAdmin(admin.ModelAdmin):
    list_display = ('title', 'age', 'description', 'price_for_one', 'price_for_month')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description')


admin.site.register(Gardens)
admin.site.register(Schedule)
admin.site.register(Group)
admin.site.register(Lessons)
