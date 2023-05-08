from rest_framework import serializers
from .models import Exercises

class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = "__all__"

