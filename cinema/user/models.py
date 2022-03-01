from django.db import models
from uuid import uuid4


class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
