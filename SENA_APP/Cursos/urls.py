from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('cursos/<int:id>/', views.detalle_curso, name='detalle_curso'),
    path('cursos/crear/', views.CursoCreateView.as_view(), name='crear_curso'),
    path('editar/<int:id>/', views.CursoUpdateView.as_view(), name='editar_curso'), 
    path('eliminar/<int:id>/', views.CursoDeleteView.as_view(), name='eliminar_curso'),
]