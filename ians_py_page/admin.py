from django.contrib import admin

from .models import Topic, Body

# Register your models here.

admin.site.register(Topic)
admin.site.register(Body)