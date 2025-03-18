import csv

from django.core.management.base import BaseCommand
from reviews.models import Comment

from api_yamdb.settings import BASE_DIR

models = Comment


class Command(BaseCommand):
    help = 'Автоматическое добаление данных в бд'

    def handle(self, *args, **options):
        source_csv_filename = (BASE_DIR / 'static/data/comments.csv')
        with open(source_csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                Comment.objects.create(
                    review_id=int(row['review_id']),
                    text=row['text'],
                    author_id=int(row['author']),
                    pub_date=row['pub_date']
                )
