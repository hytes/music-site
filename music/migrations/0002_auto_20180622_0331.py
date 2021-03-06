# Generated by Django 2.0.5 on 2018-06-22 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='song',
            name='file_type',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_title',
            field=models.CharField(max_length=750),
        ),
    ]
