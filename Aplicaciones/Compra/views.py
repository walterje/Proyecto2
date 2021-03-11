from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from  Aplicaciones.Compra.models import *
from Aplicaciones.Compra.forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#from .models import Tipo_producto
#from Aplicaciones.Compra.models import *

# Create your views here.

#def home(request):
 #   return render(request,'Aplicaciones/home.html')

def index(request):
    return render(request, 'Aplicaciones/index.html')
"""
def listarProveedor(request):
    proveedores = Proveedor.objects.all().order_by('cod_proveedor')#select *from proveedor
    contexto = {  
        'proveedores' : proveedor
    }
    return render(request,'Aplicaciones/listar_proveedor.html',contexto)
    #return render(request, 'Aplicaciones/inicio.html', {'Proveedores': proveedores})

def agregarProveedor(request):
    if request.method == 'GET':
        form = ProveedorForm()
        contexto = {
            'form':form
        }
    else:
        form = ProveedorForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
        return redirect('listar_proveedor')#para redireccionar
    return render(request,'Aplicaciones/agregar_proveedor.html',contexto)

def editarProveedor(request,cod_proveedor):
    proveedor = Proveedor.objects.get(cod=cod_proveedor)
    if request.method == 'GET':
        form = ProveedorForm( instance=proveedor)#para instanciar el proveedor ya existente
        contexto = {
            'form':form
        }
    else:
        form = ProveedorForm(request.POST,instance=proveedor)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            contexto = {
                'form':form
            }
        return redirect('listar_proveedor')#para redireccionar
    return render(request,'Aplicaciones/agregar_proveedor.html',contexto)

def eliminarProveedor(request, cod_proveedor):
    proveedor = Mascota.objects.get(cod=cod_proveedor)
    if request.method == 'POST':
        proveedor.delete()
        contexto = { 
            'proveedores': proveedor
        }
        return redirect('listar_proveedor')
        return render(request, 'Aplicaciones/eliminar_proveedor.html', contexto)
"""
    
#fuciones basadas en clases
class ProveedorList(ListView):
    model = Proveedor
    template_name = 'Aplicaciones/listar_proveedor.html'


class ProveedorCreate(CreateView):
    model = Proveedor
    form_class=ProveedorForm
    template_name = 'Aplicaciones/agregar_proveedor.html'
    success_url = reverse_lazy('listar_proveedor')

class ProveedorUpdate(UpdateView):
    model = Proveedor
    form_class=ProveedorForm
    template_name = 'Aplicaciones/agregar_proveedor.html'
    success_url = reverse_lazy('listar_proveedor')

class ProveedorDelete(DeleteView):
    model= Proveedor
    template_name = 'Aplicaciones/eliminar_proveedor.html'
    success_url = reverse_lazy('listar_proveedor')