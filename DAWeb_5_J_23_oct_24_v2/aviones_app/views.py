from django.shortcuts import render
from .models import Aviones
# Create your views here.
def listadoMateriales(request):
    losaviones=Aviones.objects.all()
    return render(request,"gestionarAviones.html",{"misaviones":losaviones})