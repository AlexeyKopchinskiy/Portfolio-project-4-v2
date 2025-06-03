from .views import booking_page
from django.urls import path
from . import views


urlpatterns = [
    path("book/", booking_page, name="booking"),
    path('confirmation/<int:reservation_id>/',
         views.booking_confirmation, name='booking_confirmation'),
]
