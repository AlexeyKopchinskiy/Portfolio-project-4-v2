from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm


def signup(request):
    """
    Handles user registration.

    - Displays the signup form.
    - Saves the new user upon valid form submission.
    - Logs in the user automatically after registration.
    - Redirects to the member page upon successful signup.
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)
            return redirect("member")  # Redirect to member page
    else:
        form = SignUpForm()

    return render(request, "users-html/signup.html", {"form": form})


@login_required
def profile(request):
    """
    Displays the user profile page.

    - Requires the user to be logged in.
    - Loads the profile page template.
    """
    return render(request, "users-html/profile.html")


@login_required
def update_profile(request):
    """
    Allows users to update their profile information.

    - Requires authentication.
    - Loads an editable profile form.
    - Saves changes if the form is valid.
    - Redirects to the profile page upon successful update.
    """
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users:profile")  # Ensure valid redirect
    else:
        form = UserUpdateForm(instance=user)  # Ensure form is created here

    return render(
        request, "users-html/update_profile.html", {"form": form}
    )  # Pass the form to the template


def custom_logout(request):
    """Logs out the user and then displays the confirmation page."""
    logout(request)  # ✅ Logs out the user first
    return render(
        request, "users-html/logout_confirmation.html"
    )  # ✅ Loads the confirmation template directly


def logout_confirmation(request):
    """Displays the logout confirmation page."""
    return render(request, "users-html/logout_confirmation.html")
