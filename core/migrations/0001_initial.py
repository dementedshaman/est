# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('data_criado', models.DateField(auto_now=True)),
                ('csv', models.FileField(upload_to='uploads/csv')),
                ('csvDel', models.CharField(max_length=1)),
                ('csvQuo', models.CharField(max_length=1)),
                ('numClasses', models.IntegerField(blank=True, null=True)),
                ('variation', models.FloatField(blank=True, null=True)),
                ('media', models.FloatField(blank=True, null=True)),
                ('moda', models.FloatField(blank=True, null=True)),
                ('mediana', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.FloatField()),
                ('fim', models.FloatField()),
                ('analise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='core.Analise')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('analise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='core.Analise')),
                ('classe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caData', to='core.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fi', models.FloatField()),
                ('fia', models.FloatField()),
                ('fri', models.FloatField()),
                ('fria', models.FloatField()),
                ('xi', models.FloatField()),
                ('perc', models.FloatField()),
                ('ang', models.FloatField()),
                ('xifi', models.FloatField()),
                ('analise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='core.Analise')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taClasses', to='core.Classe')),
            ],
        ),
    ]
