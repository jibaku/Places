# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_place_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.Category'),
        ),
        migrations.AlterField(
            model_name='place',
            name='is_public',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Is public?'),
        ),
    ]
