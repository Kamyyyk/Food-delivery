# Generated by Django 4.0.1 on 2022-01-19 10:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_votes_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='vote',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
