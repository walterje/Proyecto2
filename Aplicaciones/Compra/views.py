from django.shortcuts import render
from  Aplicaciones.Compra.models import Proveedor
#from .models import Tipo_producto
#from Aplicaciones.Compra.models import *

# Create your views here.

#def home(request):
 #   return render(request,'Aplicaciones/home.html')
      
def inicio(request):
    Proveedores = Proveedor.objects.all()
    return render(request, 'Aplicaciones/inicio.html', {'Proveedores': Proveedores})