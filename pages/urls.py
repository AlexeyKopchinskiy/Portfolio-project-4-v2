from django.urls import path
from .views import member_page, menu_page
from . import views

urlpatterns = [
    # This maps the root URL of the app to the home view.
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),  # URL for the about page.
    path("member/", member_page, name="member"),  # URL for the member page
    path("menu/", menu_page, name="menu"),  # ✅ Add the correct menu path
]
