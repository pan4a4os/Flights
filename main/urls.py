from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('portraits', views.portraits),
    path('achievement', views.achievement),
    path('about', views.about),
    path('contacts', views.contacts)
]