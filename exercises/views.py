from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Exercises
from .serializers import ExercisesSerializer
from django.shortcuts import get_object_or_404


@api_view(http_method_names=["GET", "POST"])
def list_exercises(request:Request):

    exercises = Exercises.objects.all()
    if request.method == "POST":
        data = request.data
        serializer = ExercisesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = ExercisesSerializer(instance=exercises, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def exercise_detail(request:Request, exercise_id:int):

    exercise = get_object_or_404(Exercises, pk=exercise_id)
    serializer = ExercisesSerializer(instance=exercise)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=["PUT"])
def exercise_update(request:Request, exercise_id:int):

    exercise = get_object_or_404(Exercises, pk=exercise_id)
    data = request.data
    serializer = ExercisesSerializer(instance=exercise, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["DELETE"])
def exercise_delete(request:Request, exercise_id:int):

    exercise = get_object_or_404(Exercises, pk=exercise_id)
    exercise.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

