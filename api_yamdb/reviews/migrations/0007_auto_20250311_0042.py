# Generated by Django 3.2 on 2025-03-10 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_title_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genretitle',
            old_name='genre',
            new_name='genre_id',
        ),
        migrations.RenameField(
            model_name='genretitle',
            old_name='title',
            new_name='title_id',
        ),
    ]
