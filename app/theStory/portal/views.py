from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def portal(erequest):
    return HttpResponse("Hello, Django World")
