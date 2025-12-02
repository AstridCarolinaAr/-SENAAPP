from django.shortcuts import render
from .models import Aprendiz

def main(request):
    return render(request, 'main.html')

def aprendices(request):
    aprendices = Aprendiz.objects.all()
    context = {'aprendices': aprendices}
    return render(request, 'aprendices_list.html', context)

def details(request, id):
    aprendiz = Aprendiz.objects.get(id=id)
    context = {'aprendiz': aprendiz}
    return render(request, 'detalles_aprendices.html', context)

# Create your views here.