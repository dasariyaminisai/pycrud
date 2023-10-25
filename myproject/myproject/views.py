from django.shortcuts import render
from django.http import HttpResponse

def home(request):
     return HttpResponse("this is first project")

def demo(request):
     return HttpResponse("this is second project")

def data(request):
     return HttpResponse("this is first app")
