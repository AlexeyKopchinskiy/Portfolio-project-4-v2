from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup, update_profile, profile  # Import views directly

app_name = "users"  # ✅ Must match the namespace used in main `urls.py`


urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path("profile/", update_profile, name="profile"),
    path("profile/update/", update_profile, name="update_profile"),
    path("profile/", profile, name="profile"), 

]
