from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Exercises
from .serializers import ExercisesSerializer
from django.shortcuts import get_object_or_404

class ExercisesViewset(viewsets.ViewSet):
    def list(self, request, *args,):
        queryset = Exercises.objects.all()
        serializer = ExercisesSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        exercise = get_object_or_404(Exercises, pk=pk)
        serializer = ExercisesSerializer(instance=exercise, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


