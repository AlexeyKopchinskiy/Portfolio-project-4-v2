from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Booking Status Model (Stores different reservation statuses)


class BookingStatus(models.Model):
    # Example: "Pending", "Confirmed"
    status = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.status


# Location Model (Stores seating areas)


class Location(models.Model):
    location = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.location


# Table Model (Stores table details)


class Table(models.Model):
    size = models.SmallIntegerField(null=True)  # Number of seats
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="tables"
    )

    def __str__(self):
        return f"Table {self.id} ({self.location.location})"


# Reservation Model (Handles bookings)


class Reservation(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(null=True)
    booking_time = models.TimeField(null=True)
    num_of_guests = models.PositiveSmallIntegerField(default=1)
    booking_status = models.ForeignKey(
        BookingStatus,
        on_delete=models.SET_NULL,
        null=True,
        related_name="reservations",
    )
    special_requests = models.TextField(blank=True, null=True)
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-booked_on"]

    def __str__(self):
        return f"Booking by {self.user.username} \
            on {self.booking_date} ({self.booking_status.status})"
