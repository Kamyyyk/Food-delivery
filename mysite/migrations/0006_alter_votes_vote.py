# Generated by Django 4.0.1 on 2022-01-19 10:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_alter_votes_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='vote',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
