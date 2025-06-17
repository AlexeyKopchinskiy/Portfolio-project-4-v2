from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import Reservation


# Create your views here.


def home(request):
    """Render the home page."""
    return render(
        request,
        "pages-html/home.html",
        {"welcome_message": "Welcome to our restaurant! "},
    )


def about(request):
    """Render the about page."""
    return render(request, "pages-html/about.html")


@login_required
def member_page(request):
    past_bookings = Reservation.objects.filter(user=request.user).order_by(
        "-booking_date"
    )

    return render(
        request,
        "users-html/member.html",
        {
            "user": request.user,
            "past_bookings": past_bookings,
        },
    )


def menu_page(request):
    """Renders the sushi menu page."""
    return render(request, "pages-html/menu.html")
