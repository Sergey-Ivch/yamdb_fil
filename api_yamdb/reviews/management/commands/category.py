import csv

from django.core.management.base import BaseCommand
from reviews.models import Category

from api_yamdb.settings import BASE_DIR

models = Category


class Command(BaseCommand):
    help = 'Автоматическое добаление данных в бд'

    def handle(self, *args, **options):
        source_csv_filename = (BASE_DIR / 'static/data/category.csv')
        with open(source_csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                Category.objects.create(id=row['id'], name=row['name'],
                                        slug=row['slug'])
