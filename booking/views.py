from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Reservation, Table, BookingStatus, Location


@login_required
def booking_page(request):
    if request.method == "POST":
        print("Inside POST branch!")

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
            return render(request, "booking_page.html", {
                "error": "Please select a location.",
                "locations": locations,
                "tables": tables
            })

        if not table_id:
            locations = Location.objects.all()
            tables = Table.objects.select_related("location").all()
            return render(request, "booking_page.html", {
                "error": "Please select a table.",
                "locations": locations,
                "tables": tables
            })

        # Get the location and table objects or return an error view if not found
        try:
            location = Location.objects.get(id=int(location_id))
            table = Table.objects.get(id=int(table_id))
        except (Location.DoesNotExist, Table.DoesNotExist, ValueError):
            locations = Location.objects.all()
            tables = Table.objects.select_related("location").all()
            return render(request, "booking_page.html", {
                "error": "Invalid selection.",
                "locations": locations,
                "tables": tables
            })

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
            special_requests=special_requests
        )

        print("New reservation created with ID:", new_reservation.id)

        # Redirect to the confirmation page using the new reservation's ID
        return redirect("booking_confirmation", reservation_id=new_reservation.id)

    # For GET requests, load locations and tables into context
    locations = Location.objects.all()
    tables = Table.objects.select_related("location").all()
    return render(request, "booking_page.html", {"locations": locations, "tables": tables})


def booking_confirmation(request, reservation_id):
    try:
        # Eagerly load the related Table and Location objects.
        reservation = Reservation.objects.select_related(
            'table', 'location').get(pk=reservation_id)
    except Reservation.DoesNotExist:
        return redirect("booking_page")
    return render(request, "booking_confirm.html", {"reservation": reservation})
