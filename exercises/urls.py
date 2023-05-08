from . import views
from django.urls import path


urlpatterns = [

    #CLASS_BASED
    path('', views.ExerciseListCreateView.as_view(), name="exercises_list_create"),
    path('<int:exercise_id>/', views.ExerciseRetrieveUpdateDeleteView.as_view(), name="exercises_retrieve_update_delete"),


]