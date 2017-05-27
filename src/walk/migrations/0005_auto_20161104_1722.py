# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk', '0004_auto_20161102_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='like',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='walk',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='walk',
            name='type_of_move',
            field=models.CharField(choices=[('feet', 'пешая'), ('bikes', 'велосипедная'), ('rollers', 'на роликах'), ('other', 'другой')], max_length=30),
        ),
    ]
