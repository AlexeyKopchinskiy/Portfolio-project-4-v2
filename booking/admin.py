from django.contrib import admin
from .models import Location, Table, Reservation, BookingStatus

# Register models
admin.site.register(Location)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(BookingStatus)
