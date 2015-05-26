from django.db import models

# Create your models here.

class Result(models.Model):
    term = models.CharField(max_length=200)
    document = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
