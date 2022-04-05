from .forms import WorkoutForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Workout
import datetime

def workout_list(request):
    workouts = Workout.objects.order_by('date')
    return render(request, 'journals_app/workout_list.html', {'workouts': workouts})

def workout_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'journals_app/workout_detail.html', {'workout': workout})


def new_workout(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.person = User.objects.all()[0]
            workout.date = datetime.datetime.now()
            workout.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm()
    return render(request, 'journals_app/workout_form.html', {'form': form, 'type_of_request': 'New'})

def edit_workout(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    if request.method == "POST":
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.person = User.objects.all()[0]
            workout.date = datetime.datetime.now()
            workout.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'journals_app/workout_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_workout(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    workout.delete()
    return redirect('workout_list')