# Generated by Django 4.0.1 on 2022-01-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_votes_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='pub_date',
            field=models.DateTimeField(verbose_name='data publikacji'),
        ),
    ]
