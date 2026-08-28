from django.contrib import admin
from .models import FacilityInformation, MOUHistory


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


@admin.register(MOUHistory)
class MOUHistoryAdmin(admin.ModelAdmin):
    list_display = ("facility", "mou_type", "generated_at", "status", "file_name")
    search_fields = ("facility__hospital_name", "mou_type")
    list_filter = ("status", "mou_type")
    ordering = ("-generated_at",)