# Generated by Django 4.2.7 on 2023-12-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='movie', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
