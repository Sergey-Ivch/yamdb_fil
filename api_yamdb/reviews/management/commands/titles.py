import csv

from django.core.management.base import BaseCommand
from reviews.models import Title

from api_yamdb.settings import BASE_DIR

models = Title


class Command(BaseCommand):
    help = 'Автоматическое добаление данных в бд'

    def handle(self, *args, **options):
        source_csv_filename = (BASE_DIR / 'static/data/titles.csv')
        with open(source_csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                Title.objects.create(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category_id=int(row['category'])
                )
