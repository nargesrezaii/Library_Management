# Generated by Django 4.2.15 on 2024-09-01 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanage', '0003_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='nationality',
        ),
    ]
