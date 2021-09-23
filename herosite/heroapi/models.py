# models.py

from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return str(self.name)

class Superpowers(models.Model):
    name= models.CharField(max_length=80)
    def __str__(self):
        return str(self.name)
class Hero(models.Model):
    name = models.CharField(max_length=80)
    alias = models.CharField(max_length=80)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, default=1)
    superpowers = models.ManyToManyField(Superpowers)
    def __str__(self):
        return str(self.name)
