from django import forms
from .models import FacilityInformation


class FacilityInformationForm(forms.ModelForm):

    class Meta:
        model = FacilityInformation

        fields = [
            "hospital_name",
            "hospital_address",

            "dry_cleaner_name",
            "dry_cleaner_address",

            "blood_bank_name",
            "blood_bank_address",

            "canteen_name",
            "canteen_address",

            "second_hospital_name",
            "second_hospital_address",

            "ambulance_name",
            "ambulance_address",

            "radio_lab_name",
            "radio_lab_address",

            "lab_name",
            "lab_address",
            "contract_start_date",
            "contract_end_date",
        ]

        widgets = {

            "hospital_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter hospital name"
            }),

            "hospital_address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter hospital address",
                "rows": 3
            }),

            "dry_cleaner_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter dry cleaner name"
            }),

            "dry_cleaner_address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter dry cleaner address",
                "rows": 3,
                "list": "provider-address-dry_cleaner_address",
                "data-name-field": "dry_cleaner_name",
            }),

            "blood_bank_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter blood bank name"
            }),

            "blood_bank_address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter blood bank address",
                "rows": 3,
                "list": "provider-address-blood_bank_address",
                "data-name-field": "blood_bank_name",
            }),

            "canteen_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter canteen name"
            }),

            "canteen_address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter canteen address",
                "rows": 3,
                "list": "provider-address-canteen_address",
                "data-name-field": "canteen_name",
            }),

            "second_hospital_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter second hospital name"
            }),

            "second_hospital_address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter second hospital address",
                "rows": 3,
                "list": "provider-address-second_hospital_address",
                "data-name-field": "second_hospital_name",
            }),

            "ambulance_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter ambulance service name"
            }),

            "ambulance_address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter ambulance address",
                "rows": 3,
                "list": "provider-address-ambulance_address",
                "data-name-field": "ambulance_name",
            }),

            "radio_lab_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter radio lab name"
            }),

            "radio_lab_address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter radio lab address",
                "rows": 3,
                "list": "provider-address-radio_lab_address",
                "data-name-field": "radio_lab_name",
            }),

            "lab_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter laboratory name"
            }),

            "lab_address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter laboratory address",
                "rows": 3,
                "list": "provider-address-lab_address",
                "data-name-field": "lab_name",
            }),

            "contract_start_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),

            "contract_end_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
        }

        labels = {
            "hospital_name": "Hospital Name",
            "hospital_address": "Hospital Address",

            "dry_cleaner_name": "Dry Cleaner Name",
            "dry_cleaner_address": "Dry Cleaner Address",

            "blood_bank_name": "Blood Bank Name",
            "blood_bank_address": "Blood Bank Address",

            "canteen_name": "Canteen Name",
            "canteen_address": "Canteen Address",

            "second_hospital_name": "Second Hospital Name",
            "second_hospital_address": "Second Hospital Address",

            "ambulance_name": "Ambulance Name",
            "ambulance_address": "Ambulance Address",

            "radio_lab_name": "Radio Lab Name",
            "radio_lab_address": "Radio Lab Address",

            "lab_name": "Laboratory Name",
            "lab_address": "Laboratory Address",
            "contract_start_date": "Contract Start Date",
            "contract_end_date": "Contract End Date",
        }