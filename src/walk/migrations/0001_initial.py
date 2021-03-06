# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 13:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isLike', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('type_of_move', models.CharField(choices=[(0, 'пешая'), (1, 'велосипедная'), (2, 'на роликах'), (3, 'другой')], max_length=30)),
                ('oriented_duration', models.FloatField()),
                ('oriented_extension', models.FloatField()),
                ('oriented_region', models.CharField(max_length=200)),
                ('max_points', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='walk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='walk.Walk'),
        ),
        migrations.AddField(
            model_name='comment',
            name='walk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='walk.Walk'),
        ),
    ]
