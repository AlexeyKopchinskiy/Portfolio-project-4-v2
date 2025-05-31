from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Reservation, Table, BookingStatus, Location
from .forms import SignupForm


@login_required
def booking_page(request):
    if request.method == "POST":
        table_id = request.POST.get("table")  # 🔥 Get selected table ID
        booking_date = request.POST.get("booking_date")
        booking_time = request.POST.get("booking_time")
        num_of_guests = request.POST.get("num_of_guests")
        special_requests = request.POST.get("special_requests")

        if not table_id:
            tables = Table.objects.select_related('location').all()
            return render(request, "booking/booking_page.html", {
                "error": "Please select a table.",
                "tables": tables
            })

        try:
            table = Table.objects.get(id=int(table_id))
        except (Table.DoesNotExist, ValueError):
            tables = Table.objects.select_related('location').all()
            return render(request, "booking/booking_page.html", {
                "error": "Invalid table selection",
                "tables": tables
            })

        booking_status = BookingStatus.objects.filter(
            name="Pending").first()  # 🔥 Set default status

        # 🔥 Create and save the reservation record
        new_reservation = Reservation.objects.create(
            table=table,
            user=request.user,
            booking_date=booking_date,
            booking_time=booking_time,
            num_of_guests=num_of_guests,
            booking_status=booking_status,
            special_requests=special_requests
        )

        # ✅ Redirect to confirmation page
        return redirect("booking_confirmation")

    tables = Table.objects.select_related(
        'location').all()  # 🔥 Load available tables
    return render(request, "booking/booking_page.html", {"tables": tables})


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
