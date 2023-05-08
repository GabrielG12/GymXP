from . import views
from django.urls import path


urlpatterns = [
    path('', views.list_exercises, name="exercises_list"),
    path('<int:exercise_index>/', views.list_detail, name="exercise_detail"),
]