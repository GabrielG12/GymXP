from django.db import models

class Exercises(models.Model):

    types = (("Cardio", "Cardio"), ("Strength", "Strength"), ("Technique", "Technique"))
    type = models.CharField(max_length=100, blank=False, choices=types)
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name
