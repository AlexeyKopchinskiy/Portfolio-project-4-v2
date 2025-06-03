from django import forms
from .models import Reservation


class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['location', 'table', 'booking_date',
                  'booking_time', 'num_of_guests', 'special_requests']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['table'].widget.attrs.update({'class': 'form-control'})
        self.fields['num_of_guests'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['booking_date'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['booking_time'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['special_requests'].widget.attrs.update(
            {'class': 'form-control'})
