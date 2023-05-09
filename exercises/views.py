from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from .models import Exercises
from .serializers import ExercisesSerializer
from django.shortcuts import get_object_or_404



#TODO: VIEW FOR LISTING AND CREATING AN EXERCISE
class ExerciseListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = ExercisesSerializer
    queryset = Exercises.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#TODO: VIEW FOR RETRIEVING; UPDATING AND DELETING PARTICULAR OBJECT
class ExerciseRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin):

    serializer_class = ExercisesSerializer
    queryset = Exercises.objects.all()
    # lookup_field is for url parameter
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
