from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Reservation, Table, BookingStatus, Location
from .forms import BookingForm
from django.contrib import messages
from datetime import datetime, timedelta
from datetime import date


@login_required
def booking_page(request):
    """
    Handles the main booking page where users can select a table and make a
    reservation.

    - Displays available tables.
    - Processes form submissions to create a new reservation.
    - Redirects to booking confirmation after successful reservation.
    """
    tables = Table.objects.select_related("location").all()

    if request.method == "POST":
        form = BookingForm(request.POST)

        # Manual validation: ensure table is selected
        table_id = request.POST.get("table")
        if not table_id:
            messages.error(request, "❌ Please select a table.")
            return render(
                request,
                "booking-html/booking_page.html",
                {
                    "form": form,
                    "tables": tables,
                },
            )

        # Manual validation: ensure table exists
        try:
            table = Table.objects.get(id=int(table_id))
        except (Table.DoesNotExist, ValueError):
            messages.error(request, "❌ Invalid table selection.")
            return render(
                request,
                "booking-html/booking_page.html",
                {
                    "form": form,
                    "tables": tables,
                },
            )

        # Form validation: check booking_date and other fields
        if form.is_valid():
            new_reservation = form.save(commit=False)
            new_reservation.user = request.user
            new_reservation.table = table  # ✅ Assign validated table
            new_reservation.booking_status = BookingStatus.objects.filter(
                status="Pending"
            ).first()
            new_reservation.save()
            messages.success(request, "✅ Your reservation has been created.")
            return redirect(
                "booking_confirmation", reservation_id=new_reservation.id
            )
        else:
            messages.error(request, "❌ Please correct the errors below.")
            print(form.errors)  # ✅ Debug: see what failed

    else:
        form = BookingForm()

    return render(
        request,
        "booking-html/booking_page.html",
        {
            "form": form,
            "tables": tables,
        },
    )


def booking_confirmation(request, reservation_id):
    """
    Displays the booking confirmation page with reservation details.

    - Retrieves reservation information.
    - Redirects to the booking page if reservation does not exist.
    """
    try:
        # Eagerly load the related Table and Location objects.
        reservation = Reservation.objects.select_related(
            "table", "location"
        ).get(pk=reservation_id)
    except Reservation.DoesNotExist:
        return redirect("booking_page")
    return render(
        request,
        "booking-html/booking_confirm.html",
        {"reservation": reservation},
    )


@login_required
def update_booking(request, reservation_id):
    """
    Allows users to update their booking details.

    - Fetches existing reservation and displays an editable form.
    - Saves updated information upon form submission.
    - Shows a confirmation message after successful update.
    - Redirects back to the member page.
    """
    booking = get_object_or_404(
        Reservation, id=reservation_id, user=request.user
    )
    form = BookingForm(instance=booking)
    locations = Location.objects.all()  # ✅ Fetch locations
    tables = Table.objects.all()  # ✅ Fetch tables

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(
                request, "✅ Your booking has been successfully updated!"
            )  # ✅ Confirmation message
            return redirect("member_page")  # Redirect back after updating

    return render(
        request,
        "booking-html/update_booking.html",
        {
            "form": form,
            "booking": booking,
            "locations": locations,
            "tables": tables,
        },
    )


@login_required
def delete_booking(request, reservation_id):
    """
    Handles booking cancellation.

    - Deletes the booking upon user confirmation.
    - Redirects to the member page after deletion.
    """
    booking = get_object_or_404(
        Reservation, id=reservation_id, user=request.user
    )

    if request.method == "POST":
        booking.delete()
        messages.success(
            request, "✅ Your booking has been successfully canceled!"
        )  # ✅ Confirmation message

        # ✅ Ensure this matches the correct URL name
        return redirect("member_page")

    return render(
        request, "booking-html/delete_booking.html", {"booking": booking}
    )


@login_required
def create_booking(request):
    """
    Allows users to create a new booking.

    - Displays an empty booking form.
    - Saves the booking and assigns default status after submission.
    - Redirects the user after successful creation.
    """
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
    """
    Displays the member's booking history.

    - Fetches all past bookings made by the logged-in user.
    - Orders bookings by most recent first.
    """
    past_bookings = Reservation.objects.filter(user=request.user).order_by(
        "-booking_date"
    )
    return render(
        request, "users-html/member.html", {"past_bookings": past_bookings}
    )


@login_required
def get_available_tables(request):
    """
    Retrieves available tables for a selected date and time.

    - Excludes tables that are already booked within ±1 hour of the requested
        time.
    - Returns filtered tables as a JSON response.
    """
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
            datetime.combine(booking_date, booking_time) + timedelta(hours=2)
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
                "smoking": table.smoking,
                "accessible": table.accessible,
            }
            for table in available_tables
        ]
    }

    return JsonResponse(data)


@login_required
def cancel_booking(request, reservation_id):
    """
    Handles booking cancellation.

    - Deletes the reservation upon user confirmation.
    - Redirects to a cancellation confirmation page.
    """
    booking = get_object_or_404(
        Reservation, id=reservation_id, user=request.user
    )

    if request.method == "POST":
        booking.delete()  # ✅ Remove reservation
        return redirect(
            "cancel_booking_confirm"
        )  # ✅ Redirect to confirmation page

    return render(
        request, "booking-html/cancel_booking.html", {"booking": booking}
    )


def cancel_booking_confirm(request):
    """
    Displays a confirmation message after successful booking cancellation.
    """
    return render(request, "booking-html/cancel_booking_confirm.html")
