from django.conf import settings
from django.db import models

class Workout(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    training_day = models.CharField(max_length=200)
    workouts = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.training_day