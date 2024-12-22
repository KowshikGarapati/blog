from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

# Create your views here
def home(request):
    return render(request, "home.html")

def account(request):
    if not request.session.get("loggedin_student"):
        return redirect("login")
    else:
        return render(request, "profile.html", {"student":request.session.get("loggedin_student")})

def login(request):
    return render(request, 'login.html')

def verify(request):
    email = request.POST.get("email")
    Password = request.POST.get("password")  
    try:
        student = Student.objects.get(email=email, password=Password)
        request.session['loggedin_student'] = student
        return redirect("account")
    except e:
        return redirect("login")

def logout(request):
    request.session.flush()
    return redirect("account")

def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students":students})

def student_profile(request, pin):
    return render(request, "profile.html", {"student":Student.objects.get(pin=pin)})
