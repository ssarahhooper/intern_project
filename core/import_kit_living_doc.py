from openpyxl import load_workbook
from datetime import datetime
from django.utils import timezone
from core.models import Kit


def update_kits_from_excel(file_path: str):
    wb = load_workbook(filename=file_path, data_only=True)
    sheet = wb.active

    today = datetime.now()

    name_column = 1
    location_column = 2
    next_column = 3
    start_row = 10
    end_row = 19

    data = []






