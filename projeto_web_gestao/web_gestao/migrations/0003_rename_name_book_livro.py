# Generated by Django 4.2.5 on 2023-10-16 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_gestao', '0002_rename_livro_book_rename_data_book_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='livro',
        ),
    ]
