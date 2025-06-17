from .views import (
    booking_page,
    booking_confirmation,
    update_booking,
    delete_booking,
    create_booking,
    get_available_tables,
)


from django.urls import path, include
from . import views
from .views import (
    member_page,
    get_available_tables,
    cancel_booking,
    cancel_booking_confirm,
)


urlpatterns = [
    path("booking/", booking_page, name="booking_page"),
    """
    Displays the booking page where users can select a table and make
    reservations.
    """
    path(
        "booking/<int:reservation_id>/",
        booking_confirmation,
        name="booking_confirmation",
    ),
    """
    Shows the confirmation page for a successful booking.
    Retrieves and displays reservation details.
    """
    path(
        "booking/update/<int:reservation_id>/",
        update_booking,
        name="update_booking",
    ),
    """
    Allows users to update their existing booking details.
    Fetches the current reservation and provides an editable form.
    """

    path(
        "booking/delete/<int:reservation_id>/",
        delete_booking,
        name="delete_booking",
    ),
    """
    Handles booking deletion requests.
    Deletes the selected reservation and redirects users accordingly.
    """
    path("booking/create/", create_booking, name="create_booking"),
    """
    Enables users to create a new booking.
    Displays an empty booking form and saves the reservation upon submission.
    """
    path("member/", member_page, name="member_page"),
    """
    Displays the user's past bookings.
    Orders bookings by most recent first.
    """
    path(
        "booking/delete/<int:reservation_id>/",
        delete_booking,
        name="delete_booking",
    ),
    path("summernote/", include("django_summernote.urls")),
    """
    Integrates Summernote for rich text editing, useful for special requests.
    """
    path(
        "get-available-tables/",
        get_available_tables,
        name="get_available_tables",
    ),
    """
    Fetches available tables based on user-selected date and time.
    Excludes tables already booked within ±1 hour of the requested slot.
    Returns filtered results as a JSON response.
    """
    path(
        "booking/cancel/<int:reservation_id>/",
        cancel_booking,
        name="cancel_booking",
    ),
    """
    Handles booking cancellations.
    Deletes the reservation upon user confirmation and redirects to the
    confirmation page.
    """
    path(
        "booking/cancel/confirm/",
        cancel_booking_confirm,
        name="cancel_booking_confirm",
    ),
    """
    Displays a confirmation message after successful booking cancellation.
    """
]
