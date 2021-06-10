"""Defines URL patterns for ians_py_page."""

from django.urls import path

from . import views 

app_name = 'ians_py_page'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]