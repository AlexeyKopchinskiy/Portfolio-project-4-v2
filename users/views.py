from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


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
