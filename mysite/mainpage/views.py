from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    return render(request, 'mainpage/index.html')


def portfolio(request):
    return render(request, 'mainpage/portfolio.html')


def contacts(request):
    return render(request, 'mainpage/contacts.html')