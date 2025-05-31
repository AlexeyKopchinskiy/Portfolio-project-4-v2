from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm


@login_required
def booking_page(request):
    return render(request, "booking/booking_page.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("booking")  # Redirect to booking page
    else:
        form = SignupForm()
    return render(request, "booking/signup.html", {"form": form})
