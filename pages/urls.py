from django.urls import path
from . import views

urlpatterns = [
    # This maps the root URL of the app to the home view.
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # URL for the about page.
]
