# Generated by Django 5.2.1 on 2025-06-04 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentrymodel',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Timestamp'),
        ),
    ]
