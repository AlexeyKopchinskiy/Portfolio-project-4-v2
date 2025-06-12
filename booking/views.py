from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Reservation, Table, BookingStatus, Location
from .forms import BookingForm
from datetime import datetime, timedelta


@login_required
def booking_page(request):
    form = BookingForm()

    if request.method == "POST":
        # Extract data from POST
        location_id = request.POST.get("location")
        table_id = request.POST.get("table")
        booking_date = request.POST.get("booking_date")
        booking_time = request.POST.get("booking_time")
        num_of_guests = request.POST.get("num_of_guests")
        special_requests = request.POST.get("special_requests")

        # Validate that required selections are made
        if not location_id:
            locations = Location.objects.all()
            tables = Table.objects.select_related("location").all()
            return render(
                request,
                "booking_page.html",
                {
                    "error": "Please select a location.",
                    "locations": locations,
                    "tables": tables,
                },
            )

        if not table_id:
            locations = Location.objects.all()
            tables = Table.objects.select_related("location").all()
            return render(
                request,
                "booking_page.html",
                {
                    "error": "Please select a table.",
                    "locations": locations,
                    "tables": tables,
                },
            )

        # Get the location and table objects or return an error view if
        # not found
        try:
            location = Location.objects.get(id=int(location_id))
            table = Table.objects.get(id=int(table_id))
        except (Location.DoesNotExist, Table.DoesNotExist, ValueError):
            locations = Location.objects.all()
            tables = Table.objects.select_related("location").all()
            return render(
                request,
                "booking_page.html",
                {
                    "error": "Invalid selection.",
                    "locations": locations,
                    "tables": tables,
                },
            )

        # Get the booking status (make sure the field name 'status' is correct)
        booking_status = BookingStatus.objects.filter(status="Pending").first()

        # Create the reservation and assign it to new_reservation
        new_reservation = Reservation.objects.create(
            table=table,
            location=location,
            user=request.user,
            booking_date=booking_date,
            booking_time=booking_time,
            num_of_guests=num_of_guests,
            booking_status=booking_status,
            special_requests=special_requests,
        )

        print("New reservation created with ID:", new_reservation.id)

        # Redirect to the confirmation page using the new reservation's ID
        return redirect(
            "booking_confirmation", reservation_id=new_reservation.id
        )

    # For GET requests, load locations and tables into context
    locations = Location.objects.all()
    tables = Table.objects.select_related("location").all()
    return render(
        request,
        "booking_page.html",
        {"locations": locations, "tables": tables, "form": form},
    )


def booking_confirmation(request, reservation_id):
    try:
        # Eagerly load the related Table and Location objects.
        reservation = Reservation.objects.select_related(
            "table", "location"
        ).get(pk=reservation_id)
    except Reservation.DoesNotExist:
        return redirect("booking_page")
    return render(
        request, "booking_confirm.html", {"reservation": reservation}
    )


@login_required
def update_booking(request, reservation_id):
    booking = get_object_or_404(
        Reservation, id=reservation_id, user=request.user
    )
    # booking = get_object_or_404(Reservation, id=booking_id)
    form = BookingForm(instance=booking)
    locations = Location.objects.all()  # ✅ Fetch locations
    tables = Table.objects.all()  # ✅ Fetch tables

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect("member_page")  # Redirect back after updating
    else:
        form = BookingForm(instance=booking)

    return render(
        request,
        "update_booking.html",
        {
            "form": form,
            "booking": booking,
            "locations": locations,
            "tables": tables,
        },
    )


@login_required
def delete_booking(request, reservation_id):
    booking = get_object_or_404(
        Reservation, id=reservation_id, user=request.user
    )

    if request.method == "POST":
        booking.delete()
        # ✅ Ensure this matches the correct URL name
        return redirect("member_page")

    return render(request, "delete_booking.html", {"booking": booking})


@login_required
def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.user = request.user  # Assign current user
            new_booking.booking_status = BookingStatus.objects.filter(
                status="Pending"
            ).first()
            new_booking.save()
            return redirect("member_page")  # Redirect after creating
    else:
        form = BookingForm()

    locations = Location.objects.all()
    tables = Table.objects.select_related("location").all()

    return render(
        request,
        "create_booking.html",
        {"form": form, "locations": locations, "tables": tables},
    )


@login_required
def member_page(request):
    past_bookings = Reservation.objects.filter(user=request.user).order_by(
        "-booking_date"
    )
    return render(request, "member.html", {"past_bookings": past_bookings})


@login_required
def get_available_tables(request):
    date_str = request.GET.get("date")
    time_str = request.GET.get("time")

    try:
        # ✅ Convert string to actual date & time objects
        booking_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        booking_time = datetime.strptime(time_str, "%H:%M").time()

        # ✅ Define time range (±1 hour)
        lower_bound = (
            datetime.combine(booking_date, booking_time) - timedelta(hours=1)
        ).time()
        upper_bound = (
            datetime.combine(booking_date, booking_time) + timedelta(hours=1)
        ).time()

    except ValueError:
        return JsonResponse(
            {"error": "Invalid date or time format"}, status=400
        )

    # ✅ Query booked tables within the ±1 hour range
    booked_table_ids = Reservation.objects.filter(
        booking_date=booking_date,
        booking_time__range=(
            lower_bound,
            upper_bound,
        ),  # ✅ Exclude tables booked within ±1 hour
    ).values_list("table_id", flat=True)

    # ✅ Get available tables
    available_tables = Table.objects.exclude(id__in=booked_table_ids)

    data = {
        "available_tables": [
            {
                "id": table.id,
                "size": table.size,
                "location": table.location.location,
            }
            for table in available_tables
        ]
    }

    return JsonResponse(data)
