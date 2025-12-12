from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Curso, InstructorCurso, AprendizCurso

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
