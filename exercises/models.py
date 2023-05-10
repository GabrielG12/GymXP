from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()
class Exercises(models.Model):

    types = (("Cardio", "Cardio"), ("Strength", "Strength"), ("Technique", "Technique"))
    type = models.CharField(max_length=100, blank=False, choices=types)
    name = models.CharField(max_length=150, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return self.name
