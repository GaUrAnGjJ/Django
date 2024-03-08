from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def stu2_name(request):
    return HttpResponse("<h1> Student2</h1>")