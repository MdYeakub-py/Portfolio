# Generated by Django 4.1.6 on 2023-02-06 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeakub', '0004_education_end_date_education_srt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='srt_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
