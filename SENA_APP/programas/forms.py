from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar programas"""
    
    class Meta:
        model = Programa
        fields = [
            'codigo',
            'nombre',
            'modalidad',
            'duracion_meses',
            'duracion_horas',
            'competencias',
            'requisitos_ingreso',
            'centro_formacion',
            'regional',
            'estado',
            'fecha_creacion',
            'descripcion',
            'nivel_formacion',
        
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'modalidad': forms.Select(attrs={'class': 'form-select'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'competencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'requisitos_ingreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'centro_formacion': forms.TextInput(attrs={'class': 'form-control'}),   
            'regional': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nivel_formacion': forms.Select(attrs={'class': 'form-select'}),
            'duracion_meses': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
        
        labels = {
            'codigo': 'Código del Programa',
            'nombre': 'Nombre del Programa',
            'modalidad': 'Modalidad',
            'duracion_meses': 'Duración en Meses',
            'duracion_horas': 'Duración en Horas',
            'competencias': 'Competencias a Desarrollar',
            'requisitos_ingreso': 'Requisitos de Ingreso',
            'centro_formacion': 'Centro de Formación',
            'regional': 'Regional',
            'estado': 'Estado',
            'fecha_creacion': 'Fecha de Creación del Programa',
            'descripcion': 'Descripción del Programa',
            'nivel_formacion': 'Nivel de Formación',
        }

    def clean_codigo_programa(self):
        """Validar código del programa"""
        codigo = self.cleaned_data.get('codigo_programa')
        if not codigo.isalnum():
            raise forms.ValidationError("El código del programa debe ser alfanumérico.")
        return codigo