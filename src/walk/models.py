# -*- coding: utf-8 -*-
from django.db import models
from core.models import User


class Walk(models.Model):
    description = models.TextField(blank=True)
    TYPE_OF_MOVE = (
        ('feet', 'пешая'),
        ('bikes', 'велосипедная'),
        ('rollers', 'на роликах'),
        ('other', 'другой'),)
    type_of_move = models.CharField(max_length=30, choices= TYPE_OF_MOVE)
    oriented_duration = models.FloatField()
    oriented_extension = models.FloatField()
    oriented_region = models.CharField(blank=True, max_length=200)
    created_at =  models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.description)

class Comment(models.Model):
    user = models.ForeignKey(to = User, related_name='comments')
    walk = models.ForeignKey(to = Walk, related_name='comments')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Like(models.Model):
    isLike = models.IntegerField()
    user = models.ForeignKey(to = User, related_name='likes', null=True)
    walk = models.ForeignKey(to = Walk, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)
