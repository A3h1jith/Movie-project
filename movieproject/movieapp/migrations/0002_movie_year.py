# Generated by Django 4.1.5 on 2023-01-31 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=2023),
            preserve_default=False,
        ),
    ]
