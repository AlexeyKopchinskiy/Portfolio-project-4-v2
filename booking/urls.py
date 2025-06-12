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
from .views import member_page, get_available_tables


urlpatterns = [
    # path('confirmation/<int:reservation_id>/',
    #      views.booking_confirmation, name='booking_confirmation'),
    path("booking/", booking_page, name="booking_page"),
    path(
        "booking/<int:reservation_id>/",
        booking_confirmation,
        name="booking_confirmation",
    ),
    path(
        "booking/update/<int:reservation_id>/",
        update_booking,
        name="update_booking",
    ),
    path(
        "booking/delete/<int:reservation_id>/",
        delete_booking,
        name="delete_booking",
    ),
    path("booking/create/", create_booking, name="create_booking"),
    path("member/", member_page, name="member_page"),
    # path("users/", include("users.urls", namespace="users")),
    path(
        "booking/delete/<int:reservation_id>/",
        delete_booking,
        name="delete_booking",
    ),
    path("summernote/", include("django_summernote.urls")),
    path(
        "get-available-tables/",
        get_available_tables,
        name="get_available_tables",
    ),
]
