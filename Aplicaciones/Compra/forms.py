#from django.forms import ModelForm
from django import forms
from  Aplicaciones.Compra.models import Proveedor
#para crear un formulario html de acuerdo al modelo creado
class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields = '__all__'#para que me tome todos los campos
        #fields=('cod_proveedor','nombre','ruc','telefono','direccion','timbrado','email','ciudad',)
