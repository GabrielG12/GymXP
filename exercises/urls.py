from . import views
from django.urls import path


urlpatterns = [

    #CLASS_BASED
    path('', views.ExercisesViewset.as_view(), name="exercises_list_create"),
    path('<int:id>/', views.ExerciseRetrieveUpdateDeleteView.as_view(), name="exercises_retrieve_update_delete"),


]