# Generated by Django 4.0.1 on 2022-01-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercises',
            name='burned_calories',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.IntegerField(default=1),
        ),
    ]
