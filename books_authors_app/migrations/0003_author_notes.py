# Generated by Django 2.2.4 on 2020-07-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_author_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
