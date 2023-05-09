from django.contrib import admin
from django.urls import path, include
from exercises.views import ExercisesViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", ExercisesViewset, basename="exercises")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exercises/', include(router.urls)),
]
