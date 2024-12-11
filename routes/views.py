from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here
def home(request):
    students = Student.objects.all()
    return render(request, "home.html", {"students":students})

def profile(request, pin):
    return render(request, "profile.html", {"student":Student.objects.get(pin=pin)})
