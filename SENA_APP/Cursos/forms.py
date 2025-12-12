from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'codigo',
            'nombre',
            'programa',
            'instructor_coordinador',
            'instructores',
            'aprendices',
            'fecha_inicio',
            'fecha_fin',
            'horario',
            'aula',
            'cupos_maximos',
            'estado',
            'observaciones',
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'programa': forms.Select(attrs={'class': 'form-select'}),
            'instructor_coordinador': forms.Select(attrs={'class': 'form-select'}),
            'instructores': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'aula': forms.TextInput(attrs={'class': 'form-control'}),
            'cupos_maximos': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'aprendices': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
        labels = {
            'codigo': 'Código del Curso',
            'nombre': 'Nombre del Curso',
            'programa': 'Programa de Formación',
            'instructor_coordinador': 'Instructor Coordinador',
            'instructores': 'Instructores',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_fin': 'Fecha de Finalización',
            'horario': 'Horario',
            'aula': 'Aula/Ambiente',
            'cupos_maximos': 'Cupos Máximos',
            'estado': 'Estado del Curso',
            'observaciones': 'Observaciones',
            'aprendices': 'Aprendices',
        }
        
        def clean_codigo(self):
            """Validar código del curso"""
            codigo = self.cleaned_data.get('codigo')
            if not codigo.isalnum():
                raise forms.ValidationError("El código del curso debe ser alfanumérico.")
            return codigo