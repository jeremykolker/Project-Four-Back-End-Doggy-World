from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    walk_time = models.TimeField()
    feeding_instructions = models.CharField(max_length=50)
    photo_url = models.URLField(null=True, blank=True)
