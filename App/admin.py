from django.contrib import admin
from .models import FacilityInformation


@admin.register(FacilityInformation)
class FacilityInformationAdmin(admin.ModelAdmin):
    list_display = (
        "hospital_name",
        "dry_cleaner_name",
        "blood_bank_name",
        "canteen_name",
        "second_hospital_name",
        "ambulance_name",
        "radio_lab_name",
        "lab_name",
        "created_at",
    )

    search_fields = (
        "hospital_name",
        "dry_cleaner_name",
        "blood_bank_name",
        "canteen_name",
        "second_hospital_name",
        "ambulance_name",
        "radio_lab_name",
        "lab_name",
    )

    ordering = ("-created_at",)