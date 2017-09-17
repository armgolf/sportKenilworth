from django.db import models
from django.utils import timezone

class Clubs(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField()
    cost = models.CharField(max_length=100)
    contact = models.EmailField(max_length=254, default="youremail@xname.com")
    website = models.CharField(max_length=100, default="dave@XSport.co.uk")
    getstarted = models.CharField(max_length=200, default="How to try it out?")
    image = models.CharField(max_length=500, default="imagelinkhere")

class Events(models.Model):
    event = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=200, default="Event location here")
