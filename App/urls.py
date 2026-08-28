from django.urls import path
from . import views


urlpatterns = [

    path("dashboard/", views.dashboard, name="dashboard"),
    path("facilities/", views.facility_list, name="facility_list"),
    path("facilities/add/", views.facility_add, name="facility_add"),
    path("facilities/<int:facility_id>/", views.facility_detail, name="facility_detail"),
    path("facilities/<int:facility_id>/edit/", views.facility_edit, name="facility_edit"),
    path("facilities/<int:facility_id>/delete/", views.facility_delete, name="facility_delete"),
    path("mous/", views.mou_documents, name="mou_documents"),
    path("mous/generate/", views.generate_mou_page, name="generate_mou_page"),
    path("mou-history/", views.mou_history, name="mou_history"),
    path("mou-history/<int:history_id>/download/", views.download_history, name="download_history"),

    path("", views.dashboard, name="home"),
    path("facility-information/", views.facility_information, name="facility_information"),

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