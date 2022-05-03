from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("an awesome dashboard is on its way")

# Create your views here.


