import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from docx import Document

from .forms import FacilityInformationForm
from .models import FacilityInformation

TEMPLATE_FILES = {
    "ambulance": "ambulance.docx",
    "blood_bank": "blood_bank.docx",
    "canteen": "canteen.docx",
    "second_hospital": "second_hospital.docx",
    "lab": "lab.docx",
    "radio_lab": "radio_lab.docx",
    "dry_cleaner": "dry_cleaner.docx",
}


def facility_information(request):
    if request.method == "POST":
        form = FacilityInformationForm(request.POST)
        if form.is_valid():
            facility = form.save()
            return redirect("mou_list", facility_id=facility.id)
    else:
        form = FacilityInformationForm()

    return render(request, "facility_information.html", {"form": form})


def mou_list(request, facility_id):
    facility = get_object_or_404(FacilityInformation, id=facility_id)
    return render(request, "mou_list.html", {"facility": facility})


def _build_replacements(facility):
    values = {
        "{hospital_name}": facility.hospital_name or "",
        "{HOSPITAL_NAME}": facility.hospital_name or "",
        "{hospital_address}": facility.hospital_address or "",
        "{HOSPITAL_ADDRESS}": facility.hospital_address or "",
        "{dry_cleaner_name}": facility.dry_cleaner_name or "",
        "{DRY_CLEANER_NAME}": facility.dry_cleaner_name or "",
        "{dry_cleaner_address}": facility.dry_cleaner_address or "",
        "{DRY_CLEANER_ADDRESS}": facility.dry_cleaner_address or "",
        "{blood_bank_name}": facility.blood_bank_name or "",
        "{BLOOD_BANK_NAME}": facility.blood_bank_name or "",
        "{blood_bank_address}": facility.blood_bank_address or "",
        "{BLOOD_BANK_ADDRESS}": facility.blood_bank_address or "",
        "{canteen_name}": facility.canteen_name or "",
        "{CANTEEN_NAME}": facility.canteen_name or "",
        "{canteen_address}": facility.canteen_address or "",
        "{CANTEEN_ADDRESS}": facility.canteen_address or "",
        "{second_hospital_name}": facility.second_hospital_name or "",
        "{SECOND_HOSPITAL_NAME}": facility.second_hospital_name or "",
        "{second_hospital_address}": facility.second_hospital_address or "",
        "{SECOND_HOSPITAL_ADDRESS}": facility.second_hospital_address or "",
        "{ambulance_name}": facility.ambulance_name or "",
        "{AMBULANCE_NAME}": facility.ambulance_name or "",
        "{ambulance_address}": facility.ambulance_address or "",
        "{AMBULANCE_ADDRESS}": facility.ambulance_address or "",
        "{radio_lab_name}": facility.radio_lab_name or "",
        "{RADIO_LAB_NAME}": facility.radio_lab_name or "",
        "{radio_lab_address}": facility.radio_lab_address or "",
        "{RADIO_LAB_ADDRESS}": facility.radio_lab_address or "",
        "{lab_name}": facility.lab_name or "",
        "{LAB_NAME}": facility.lab_name or "",
        "{lab_address}": facility.lab_address or "",
        "{LAB_ADDRESS}": facility.lab_address or "",
    }
    return values


def replace_text_in_paragraph(paragraph, replacements):
    full_text = paragraph.text
    if not full_text:
        return

    updated = full_text
    for placeholder, value in replacements.items():
        updated = updated.replace(placeholder, str(value))

    if updated != full_text:
        paragraph.text = updated


def replace_text_in_table(table, replacements):
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                replace_text_in_paragraph(paragraph, replacements)
            for nested_table in cell.tables:
                replace_text_in_table(nested_table, replacements)


def replace_text_in_document(document, replacements):
    for paragraph in document.paragraphs:
        replace_text_in_paragraph(paragraph, replacements)

    for table in document.tables:
        replace_text_in_table(table, replacements)


def generate_mou(request, facility_id, mou_type):
    facility = get_object_or_404(FacilityInformation, id=facility_id)

    normalized_type = mou_type.strip().lower()
    template_name = TEMPLATE_FILES.get(normalized_type)

    if not template_name:
        return HttpResponse("Invalid MOU type.", status=400)

    template_path = os.path.join(settings.BASE_DIR, "App", "mou_templates", template_name)

    if not os.path.exists(template_path):
        return HttpResponse(f"MOU template not found: {template_name}", status=404)

    document = Document(template_path)
    replacements = _build_replacements(facility)
    replace_text_in_document(document, replacements)

    output_directory = os.path.join(settings.BASE_DIR, "generated_mous")
    os.makedirs(output_directory, exist_ok=True)

    output_file = os.path.join(output_directory, f"{normalized_type}_MOU_{facility.id}.docx")
    document.save(output_file)

    with open(output_file, "rb") as file:
        response = HttpResponse(file.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    response["Content-Disposition"] = f'attachment; filename="{normalized_type}_MOU.docx"'
    return response