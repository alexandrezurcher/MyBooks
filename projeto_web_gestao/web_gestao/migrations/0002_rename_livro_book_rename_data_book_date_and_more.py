# Generated by Django 4.2.5 on 2023-10-13 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_gestao', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Livro',
            new_name='Book',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='finalizado',
            new_name='ended',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='resenha',
            new_name='resume',
        ),
    ]
