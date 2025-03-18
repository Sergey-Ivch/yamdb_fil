import csv

# import os
from django.core.management.base import BaseCommand
from reviews.models import GenreTitle

from api_yamdb.settings import BASE_DIR

models = GenreTitle


class Command(BaseCommand):
    help = 'Автоматическое добаление данных в бд'

    def handle(self, *args, **options):
        source_csv_filename = (BASE_DIR / 'static/data/genre_title.csv')
        with open(source_csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                GenreTitle.objects.create(
                    id=row['id'],
                    title_id=int(row['title_id']),
                    genre_id=int(row['genre_id'])
                )
