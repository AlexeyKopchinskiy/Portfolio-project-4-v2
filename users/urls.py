from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup, update_profile, profile  # Import views directly

app_name = "users"  # ✅ Must match the namespace used in main `urls.py`

"""
This module defines URL patterns for user authentication and profile
management.

Includes:
- User signup
- Login/logout functionality
- Profile viewing and updates
"""
urlpatterns = [
    # Handles user registration.
    # Displays a signup form, processes user input, and redirects upon
    # successful signup.
    path("signup/", signup, name="signup"),
    # Handles user login.
    # Uses Django's built-in authentication view with a custom template.
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users-html/login.html"),
        name="login",
    ),
    # Logs out the user and redirects to the appropriate page.
    # Uses Django's built-in logout functionality.
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # Allows users to update their profile information.
    # Requires authentication and loads an editable profile form.
    path("profile/update/", update_profile, name="update_profile"),
    # Displays the user's profile page.
    path("profile/", profile, name="profile"),
]
