from . import views
from django.urls import path


urlpatterns = [
    path('', views.list_exercises, name="exercises_list"),
    path('<int:exercise_id>/', views.exercise_detail, name="exercise_detail"),
    path('update/<int:exercise_id>/', views.exercise_update, name="exercise_update"),
    path('delete/<int:exercise_id>/', views.exercise_delete, name="exercise_delete"),
]