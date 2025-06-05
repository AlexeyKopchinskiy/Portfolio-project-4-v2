from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)
            return redirect("member")  # Redirect to member page
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users:profile")  # Ensure valid redirect
    else:
        form = UserUpdateForm(instance=user)  # Ensure form is created here

    return render(
        request, "update_profile.html", {"form": form}
    )  # Pass the form to the template
