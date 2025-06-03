from .views import booking_page, booking_confirmation, update_booking, delete_booking, create_booking
from django.urls import path
from . import views


urlpatterns = [
    # path('confirmation/<int:reservation_id>/',
    #      views.booking_confirmation, name='booking_confirmation'),
    path('', booking_page, name='booking_page'),
    path('<int:reservation_id>/',
         booking_confirmation, name='booking_confirmation'),
    path('update/<int:reservation_id>/',
         update_booking, name='update_booking'),
    path('delete/<int:reservation_id>/',
         delete_booking, name='delete_booking'),
    path('create/', create_booking, name='create_booking'),
]
