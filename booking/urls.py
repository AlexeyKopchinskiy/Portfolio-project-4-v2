from .views import booking_page, signup
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"),
         name="login"),
    path("book/", booking_page, name="booking"),
    path("signup/", signup, name="signup"),
]
