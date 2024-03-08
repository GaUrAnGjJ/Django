from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student_name(request):
    return HttpResponse("<h1>Gaurang</h1>")

def student_age(request):
    return HttpResponse("<h1>20</h1>")
