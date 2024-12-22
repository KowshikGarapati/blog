from django.urls import path
from . import views

urlpatterns = [
        path("", views.account, name="account"),
        path("home", views.home, name="home"),
        path("login", views.login, name="login"),
        path("login/verify", views.verify, name="verify"),
            path("students/<str:pin>", views.student_profile, name="student_profile"),
            path("students", views.students, name="students"),
        ]
