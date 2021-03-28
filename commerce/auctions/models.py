from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    category = models.CharField(max_length=64)
    start_bid = models.IntegerField()
    current_bid = models.IntegerField(default=start_bid)

    def __str__(self):
        return f"{self.name} currently at {self.current_bid}"

class TestClass(models.Model):
    name = models.CharField(max_length=32)
    kesukaan = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name} paling suka {self.kesukaan}"