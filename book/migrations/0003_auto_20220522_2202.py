# Generated by Django 3.2.9 on 2022-05-22 19:02

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_newginindex'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='book',
            name='NewGinIndex',
        ),
        migrations.AddIndex(
            model_name='book',
            index=django.contrib.postgres.indexes.GinIndex(fields=['title'], name='NewGinIndex', opclasses=['gin_trgm_ops']),
        ),
    ]
