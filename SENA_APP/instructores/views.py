from django.shortcuts import render
from .models import Instructor

def main(request):
    return render(request, 'main.html')

def instructores(request):
    instructores = Instructor.objects.all()
    context = {'instructores': instructores}
    return render(request, 'instructores_list.html', context)

def details(request, id):
    instructor = Instructor.objects.get(id=id)
    context = {'instructor': instructor}
    return render(request, 'detalles_instructores.html', context)

# Create your views here.