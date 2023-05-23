from django.db import models

# Create your models here.
class Temprature(models.Model):
    temprature = models.IntegerField()
    time = models.DateField()