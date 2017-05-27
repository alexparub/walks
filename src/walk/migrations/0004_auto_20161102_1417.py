# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk', '0003_auto_20161102_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walk',
            name='oriented_region',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='walk',
            name='type_of_move',
            field=models.CharField(choices=[('пешая', 'пешая'), ('велосипедная', 'велосипедная'), ('на роликах', 'на роликах'), ('другой', 'другой')], max_length=30),
        ),
    ]
