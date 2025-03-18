import csv

from django.core.management.base import BaseCommand
from reviews.models import Review

from api_yamdb.settings import BASE_DIR

models = Review


class Command(BaseCommand):
    help = 'Автоматическое добаление данных в бд'

    def handle(self, *args, **options):
        source_csv_filename = (BASE_DIR / 'static/data/review.csv')
        with open(source_csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                Review.objects.create(
                    title_id=int(row['title_id']),
                    text=row['text'],
                    author_id=int(row['author']),
                    score=row['score'],
                    pub_date=row['pub_date']
                )
