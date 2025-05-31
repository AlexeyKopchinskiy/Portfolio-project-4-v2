from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Reservation, Table, BookingStatus, Location
from .forms import SignupForm


@login_required
def booking_page(request):
    if request.method == "POST":
        location_id = request.POST.get("location")
        table_id = request.POST.get("table")
        booking_date = request.POST.get("booking_date")
        booking_time = request.POST.get("booking_time")
        num_of_guests = request.POST.get("num_of_guests")
        special_requests = request.POST.get("special_requests")

        # Ensure a location was selected
        if not location_id:
            locations = Location.objects.all()
            tables = Table.objects.select_related(
                "location").all()  # all tables
            return render(request, "booking/booking_page.html", {
                "error": "Please select a location.",
                "locations": locations,
                "tables": tables
            })

        # Ensure a table was selected
        if not table_id:
            locations = Location.objects.all()
            tables = Table.objects.select_related("location").all()
            return render(request, "booking/booking_page.html", {
                "error": "Please select a table.",
                "locations": locations,
                "tables": tables
            })

        try:
            location = Location.objects.get(id=int(location_id))
            table = Table.objects.get(id=int(table_id))
        except (Location.DoesNotExist, Table.DoesNotExist, ValueError):
            locations = Location.objects.all()
            tables = Table.objects.select_related("location").all()
            return render(request, "booking/booking_page.html", {
                "error": "Invalid selection.",
                "locations": locations,
                "tables": tables
            })

        booking_status = BookingStatus.objects.filter(name="Pending").first()

        # Create the reservation record using the selected location and table.
        new_reservation = Reservation.objects.create(
            table=table,
            location=location,  # storing the selected location
            user=request.user,
            booking_date=booking_date,
            booking_time=booking_time,
            num_of_guests=num_of_guests,
            booking_status=booking_status,
            special_requests=special_requests
        )

        return redirect("booking_confirmation")

    # For GET requests, fetch all locations and tables.
    locations = Location.objects.all()
    tables = Table.objects.select_related("location").all()
    return render(request, "booking/booking_page.html", {"locations": locations, "tables": tables})


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
