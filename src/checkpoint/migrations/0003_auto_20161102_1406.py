# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkpoint', '0002_place_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
