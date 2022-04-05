from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('<int:workout_id>', views.workout_detail, name='workout_detail'),
    path('new', views.new_workout, name='new_workout'),
    path('<int:workout_id>/edit', views.edit_workout, name='edit_workout'),
    path('<int:workout_id>/delete', views.delete_workout, name='delete_workout'),
]