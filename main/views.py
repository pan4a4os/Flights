from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def portraits(request):
    return render(request, 'main/portraits.html')


def achievement(request):
    return render(request, 'main/achievement.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')