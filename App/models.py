from django.db import models


class FacilityInformation(models.Model):

    # Hospital
    hospital_name = models.CharField(max_length=255)
    hospital_address = models.TextField()

    # Dry Cleaner
    dry_cleaner_name = models.CharField(max_length=255, blank=True)
    dry_cleaner_address = models.TextField(blank=True)

    # Blood Bank
    blood_bank_name = models.CharField(max_length=255, blank=True)
    blood_bank_address = models.TextField(blank=True)

    # Canteen
    canteen_name = models.CharField(max_length=255, blank=True)
    canteen_address = models.TextField(blank=True)

    # Second Hospital
    second_hospital_name = models.CharField(max_length=255, blank=True)
    second_hospital_address = models.TextField(blank=True)

    # Ambulance
    ambulance_name = models.CharField(max_length=255, blank=True)
    ambulance_address = models.TextField(blank=True)

    # Radio Lab
    radio_lab_name = models.CharField(max_length=255, blank=True)
    radio_lab_address = models.TextField(blank=True)

    # Lab
    lab_name = models.CharField(max_length=255, blank=True)
    lab_address = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital_name

    class Meta:
        verbose_name = "Facility Information"
        verbose_name_plural = "Facility Information"
        ordering = ["-created_at"]