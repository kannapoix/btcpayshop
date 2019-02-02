from django.urls import path

from . import views

urlpatterns = [
    path('', views.about_this_site, name='about_this_site'),
]
