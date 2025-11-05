from django.core.management.base import BaseCommand
from core.import_kit_living_doc import update_kits_from_excel


class Command(BaseCommand):
    help = "Update kits from an Excel file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        update_kits_from_excel(file_path)
        self.stdout.write(self.style.SUCCESS(f"Kits updated from {file_path}"))
