# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-12 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analise',
            name='desvio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
