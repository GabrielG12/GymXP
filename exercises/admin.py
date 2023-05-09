from django.contrib import admin
from .models import Exercises

@admin.register(Exercises)

#TODO: TUKAJ POVEMO KAJ LAHKO ADMIN VIDI
class ExercisesAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    search_fields = ['name']
