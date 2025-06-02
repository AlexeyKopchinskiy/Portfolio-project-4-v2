from .views import booking_page
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import signup
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"),
         name="login"),
    path("book/", booking_page, name="booking"),
    # path('book/', views.booking_page, name='booking_page'),

    path("signup/", signup, name="signup"),
    # path('confirmation/', views.booking_confirmation,
    #      name='booking_confirmation'),
    path('confirmation/<int:reservation_id>/',
         views.booking_confirmation, name='booking_confirmation'),

]
