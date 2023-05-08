from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


exercises = [
    {
        "type": "Cardio",
        "name": "Running",
        "username": "ggjorshevski",
    },
    {
        "type": "Cardio",
        "name": "Skipping",
        "username": "johndoe",
    }
]

@api_view(http_method_names=["GET"])
def list_exercises(request:Request):
    return Response(data=exercises, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def list_detail(request:Request, exercise_index:int):
    exercise = exercises[exercise_index]
    if exercise:
        return Response(data=exercise, status=status.HTTP_201_CREATED)
    return Response(data={"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
