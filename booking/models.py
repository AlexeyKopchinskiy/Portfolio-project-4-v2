from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BookingStatus(models.Model):
    """Represents the status of a booking (e.g., Pending, Confirmed)."""

    status = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.status


class Location(models.Model):
    """Represents different seating areas within the restaurant."""

    location = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.location


class Table(models.Model):
    """Represents individual tables available for reservations."""

    size = models.SmallIntegerField(null=True)  # Number of seats
    smoking = models.BooleanField(default=False)  # ✅ Smoking area?
    accessible = models.BooleanField(default=False)  # ✅ Accessible table?
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="tables"
    )

    def __str__(self):
        return f"Table {self.id} ({self.location.location})"


class Reservation(models.Model):
    """Represents a customer's table reservation."""

    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="reservations"
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reservations",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # The user making the reservation
    booking_date = models.DateField(null=True)  # The date of the reservation
    booking_time = models.TimeField(null=True)  # The time of the reservation
    num_of_guests = models.PositiveSmallIntegerField(
        default=1
    )  # The number of guests
    booking_status = models.ForeignKey(
        BookingStatus,
        on_delete=models.SET_NULL,
        null=True,
        related_name="reservations",
    )  # The status of the booking
    special_requests = models.TextField(
        blank=True, null=True
    )  # Optional special requests by the customer
    booked_on = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the reservation was created

    class Meta:
        """Orders reservations by most recently booked first."""

        ordering = ["-booked_on"]

    def __str__(self):
        """Returns a string representation of the reservation details."""
        return f"Booking by {self.user.username} \
            on {self.booking_date} ({self.booking_status.status})"
