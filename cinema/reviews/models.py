from django.db import models
from user.models import User


class Actor(models.Model):
    name = models.CharField(max_length=32)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Biography(models.Model):
    text = models.TextField()
    actor = models.OneToOneField(Actor, on_delete=models.CASCADE)


class Cinema(models.Model):
    name = models.CharField(max_length=32)
    actors = models.ManyToManyField(Actor)


class Hero(models.Model):
    name = models.CharField(max_length=32)
    actor = models.ForeignKey(Actor, models.PROTECT)


class Review(models.Model):
    is_positive = models.BooleanField(default=True)
    text = models.TextField()
    user = models.ForeignKey(User, models.PROTECT)
    cinema = models.ForeignKey(Cinema, models.PROTECT)
