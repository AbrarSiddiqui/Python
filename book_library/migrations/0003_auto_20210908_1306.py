# Generated by Django 3.2.7 on 2021-09-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_library', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='def', max_length=50),
        ),
    ]
