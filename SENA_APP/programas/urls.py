from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('', views.programas, name='programas'),
    path('<int:programa_id>/', views.detalle_programa, name='detalle_programa'),
    path('crear/', views.ProgramaCreateView.as_view(), name='crear_programa'),
    path('editar/<int:programa_id>/', views.ProgramaUpdateView.as_view(), name='editar_programa'),
    path('eliminar/<int:programa_id>/', views.ProgramaDeleteView.as_view(), name='eliminar_programa'),
]
