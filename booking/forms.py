from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Reservation
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    """
    Allows users to create a new booking.

    - Displays an empty booking form.
    - Saves the booking and assigns default status after submission.
    - Redirects the user after successful creation.
    """

    class Meta:
        model = Reservation
        fields = [
            "table",
            "booking_date",
            "booking_time",
            "num_of_guests",
            "special_requests",
        ]
        widgets = {
            "booking_date": forms.DateInput(attrs={"type": "date"}),
            "booking_time": forms.TimeInput(attrs={"type": "time"}),
            "special_requests": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["table"].widget.attrs.update({"class": "form-control"})
        self.fields["num_of_guests"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["booking_date"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["booking_time"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["special_requests"].widget.attrs.update(
            {"class": "form-control, summernote-editor"}
        )

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get("booking_date")

        if booking_date and booking_date < date.today():
            self.add_error(
                "booking_date", "❌ You cannot book a table in the past."
            )
            raise ValidationError("Note: Booking date cannot be in the past.")
