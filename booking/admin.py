from django.contrib import admin
from .models import Location, Table, Reservation

# Register models
admin.site.register(Location)
admin.site.register(Table)
admin.site.register(Reservation)
