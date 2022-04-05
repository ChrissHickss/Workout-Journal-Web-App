from django.contrib import admin # brings in the admin ability
from .models import Workout # brings in your Workout model from the models.py file

admin.site.register(Workout) # registers Workout with your admin ability