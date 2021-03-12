#from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
#from Aplicaciones.Compra import views
urlpatterns = [
    path('',index,name='index'),
    #path('agregar_proveedor',agregarProveedor, name ="agregar_proveedor"),
    #path('listar_proveedor',listar_proveedor, name ="listar_proveedor"),
    #path('editar_proveedor',editarProveedor, name ="editar_proveedor"),
    #path('eliminar_proveedor',eliminarProveedor, name ="eliminar_proveedor"),
    path('agregar_proveedor/',ProveedorCreate.as_view(),name="agregar_proveedor"),
    path('listar_proveedor',ProveedorList.as_view(),name ="listar_proveedor"),
    path('editar_proveedor/<int:pk>/',ProveedorUpdate.as_view(),name ="editar_proveedor"),
    path('eliminar_proveedor/<int:pk>/',ProveedorDelete.as_view(),name="eliminar_proveedor")
    
    
    
]
