from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Exercises
from .serializers import ExercisesSerializer
from django.shortcuts import get_object_or_404


#TODO: VIEW FOR LISTING AND CREATING AN EXERCISE
class ExerciseListCreateView(APIView):

    serializer_class = ExercisesSerializer
    def get(self, request, *args, **kwargs):

        exercises = Exercises.objects.all()
        serializer = ExercisesSerializer(instance=exercises, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseRetrieveUpdateDeleteView(APIView):

    serializer_class = ExercisesSerializer

    def get(self, request, exercise_id:int):
        exercise = get_object_or_404(Exercises, pk=exercise_id)
        serializer = self.serializer_class(instance=exercise)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, exercise_id:int):
        exercise = get_object_or_404(Exercises, pk=exercise_id)
        data = request.data
        serializer = self.serializer_class(instance=exercise, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, exercise_id:int):
        exercise = get_object_or_404(Exercises, pk=exercise_id)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)