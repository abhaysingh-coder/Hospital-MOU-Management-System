from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.facility_information,
        name="facility_information"
    ),

    path(
        "mou/<int:facility_id>/",
        views.mou_list,
        name="mou_list"
    ),

    path(
        "mou/<int:facility_id>/<str:mou_type>/",
        views.generate_mou,
        name="generate_mou"
    ),
]