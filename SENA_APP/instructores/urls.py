from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [

    path('instructores/', views.instructores, name='instructores'),
    path('instructor/<int:id>', views.details, name='details'),
]