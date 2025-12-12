from django.http import HttpResponse
from django.template import loader
from .models import Programa

from .forms import ProgramaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def programas(request):
    lista_programas = Programa.objects.all().values()
    template = loader.get_template("lista_programas.html")
    context = {
        "lista_programas": lista_programas,
        'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))


def detalle_programa(request, programa_id):
    programa_detalle = Programa.objects.get(id=programa_id)
    template = loader.get_template("programa_detalle.html")
    context = {
        "programa_detalle": programa_detalle,
    }
    return HttpResponse(template.render(context, request))

class ProgramaCreateView(generic.CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'crear_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    
    def form_valid(self, form):
        messages.success(self.request, 
        f'Programa {form.instance.nombre_completo} creado exitosamente.')
        return super().form_valid(form) 
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al registrar el programa. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)
    
class ProgramaUpdateView(generic.UpdateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    pk_url_kwarg = 'programa_id'

    def form_valid(self, form):
        messages.success(self.request, 
        f'Programa {form.instance.nombre_completo} actualizado exitosamente.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al actualizar el programa. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)
    
class ProgramaDeleteView(generic.DeleteView):
    model = Programa
    template_name = 'eliminar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    pk_url_kwarg = 'programa_id'
    
    def delete(self, request, *args, **kwargs):
        programa = self.get_object()
        messages.success(self.request, 
        f'Programa {programa.nombre_completo} eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)