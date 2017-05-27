from django.db import models
from core.models import User
from walk.models import Walk


class Place(models.Model):
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.address

class Puzzle(models.Model):
    puzzle_object = models.CharField(max_length=400)
    question = models.TextField()
    answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.puzzle_object + ': ' + self.question

class CheckPoint(models.Model):
    place = models.ForeignKey(to = Place, related_name='checkpoints')
    puzzle = models.ForeignKey(to = Puzzle, related_name='checkpoints')
    walk = models.ForeignKey(to = Walk, related_name='checkpoints')
    index_number = models.IntegerField()
    points = models.IntegerField(default=0)
    is_bonus = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.place.address

class UserAnswer(models.Model):
    user = models.ForeignKey(to = User, related_name='user_answers')
    puzzle = models.ForeignKey(to = Puzzle, related_name='user_answers')
    answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user + ':' + self.answer