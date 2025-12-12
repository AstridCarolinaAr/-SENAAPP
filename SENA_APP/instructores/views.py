from django.shortcuts import render
from .models import Instructor

from .forms import InstructorForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

def main(request):
    return render(request, 'main.html')

def instructores(request):
    instructores = Instructor.objects.all()
    total_instructores = instructores.count()
    context = {'instructores': instructores, 'total_instructores': total_instructores}
    return render(request, 'instructores_list.html', context)

def details(request, instructor_id):
    instructor = Instructor.objects.get(id=instructor_id)
    context = {'instructor': instructor}
    return render(request, 'detalles_instructores.html', context)

class InstructorCreateView(generic.CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'crear_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    
    def form_valid(self, form):
        messages.success(self.request, 
        f'Instructor {form.instance.nombre_completo()} creado exitosamente.')
        return super().form_valid(form) 
    
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al registrar el instructor. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)
    
    
class InstructorUpdateView(generic.UpdateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    pk_url_kwarg = 'instructor_id'

    def form_valid(self, form):
        messages.success(self.request, 
        f'Instructor {form.instance.nombre_completo()} actualizado exitosamente.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al actualizar el instructor. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)

class InstructorDeleteView(generic.DeleteView):
    model = Instructor
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    pk_url_kwarg = 'instructor_id'

    def delete(self, request, *args, **kwargs):
        instructor = self.get_object()
        messages.success(self.request, 
        f'Instructor {instructor.nombre_completo()} eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

    