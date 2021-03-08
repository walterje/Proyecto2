#from django.contrib import admin
from django.urls import path
from .views import *
#from Aplicaciones.Compra import views
urlpatterns = [
    path('',inicio, name ="home"),
    path('proveedores/',inicio,name="proveedores"),

]
