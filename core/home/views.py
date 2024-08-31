from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student

people = [

    {'name':'neel','age':23},
    {'name':'madhur','age':17},
    {'name':'parth','age':22},
    {'name':'kabeer','age':23},
]



def home(req):
    return HttpResponse('<h1>hey i am a django server</h1>')

def success_page(req):

    students = Student.objects.all()
    return render(req,'home/index.html',{'people':people,'students':students})

def about(req):
    return render(req,"home/about.html")


