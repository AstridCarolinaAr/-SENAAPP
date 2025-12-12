from django.urls import path
from . import views

app_name = 'Cursos'

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('<int:id>/', views.detalle_curso, name='detalle_curso'),
]