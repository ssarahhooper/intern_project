from openpyxl import load_workbook
from datetime import datetime
from django.utils import timezone
from core.models import Kit


def update_kits_from_excel(file_path: str):
    wb = load_workbook(filename=file_path, data_only=True)
    sheet = wb.active

    today = timezone.now()

    name_column = 1
    location_column = 2
    next_column = 3
    start_row = 10
    end_row = 19

    for row in sheet.iter_rows(min_row=start_row, max_row=end_row):
        name = row[name_column - 1].value
        location = row[location_column - 1].value
        next_location = row[next_column - 1].value

        if not name:
            continue

        while next_location in (None, "Setup", "Travel"):
            next_column += 1
            next_location = sheet.cell(row=row[0].row, column=next_column).value
            if next_column > sheet.max_column:
                break

        kit, created = Kit.objects.get_or_create(name=name)
        kit.location = location
        kit.last_updated = today
        kit.destination_location = next_location
        kit.save()

        print(f"{'Created' if created else 'Updated'} kit {kit.name} -> next action: {kit.destination_location}")








