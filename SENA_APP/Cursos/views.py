from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Curso, InstructorCurso, AprendizCurso

from .forms import CursoForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

def cursos(request):
    varcursos = Curso.objects.all()
    template = loader.get_template("lista_cursos.html")
    context = {
        "varcursos": varcursos,
    }
    return HttpResponse(template.render(context, request))

def detalle_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    instructores_curso = InstructorCurso.objects.filter(curso=curso)
    aprendices_curso = AprendizCurso.objects.filter(curso=curso)
    template = loader.get_template("detalles_cursos.html")
    context = {
        "curso": curso,
        "instructores_curso": instructores_curso,
        "aprendices_curso": aprendices_curso,
    }
    return HttpResponse(template.render(context, request))

class CursoCreateView(generic.CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'crear_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    
    def form_valid(self, form):
        messages.success(self.request, 
        f'Curso {form.instance.__str__} creado exitosamente.')
        return super().form_valid(form) 
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al registrar el curso. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)
    
class CursoUpdateView(generic.UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, 
        f'Curso {form.instance.__str__} actualizado exitosamente.')
        return super().form_valid(form) 
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al actualizar el curso. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)
    
class CursoDeleteView(generic.DeleteView):
    model = Curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'id'
    
    def delete(self, request, *args, **kwargs):
        curso = self.get_object()
        messages.success(self.request,
        f'Curso {curso.__str__} eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
