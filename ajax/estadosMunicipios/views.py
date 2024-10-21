from django.shortcuts import render
from django.http import JsonResponse
from .models import Municipio
from .models import Estado

def cargar_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = Municipio.objects.filter(estado_id=estado_id).all()
    return JsonResponse(list(municipios.values('id', 'nombre')), safe=False)

def index(request):
    estados = Estado.objects.all()
    return render(request, 'index.html', {'estados': estados})

