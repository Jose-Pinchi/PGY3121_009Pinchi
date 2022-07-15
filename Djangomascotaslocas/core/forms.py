from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Genero, Cliente, Tamanio, Producto


class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'apellido', 'genero','correo','telefono','direccion']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'apellido': 'Apellido', 
            'correo': 'Correo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'genero': 'Genero',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un nombre', 
                    'id': 'nombre'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un apellido', 
                    'id': 'apellido'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un correo', 
                    'id': 'correo'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un telefono', 
                    'id': 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese una direccion', 
                    'id': 'direccion'
                }
            ),
            'genero': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'genero',
                }
            ),

        }

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['codigo', 'nombre', 'precio', 'tamanio']
        labels ={
            'codigo': 'Codigo', 
            'nombre': 'Nombre', 
            'precio': 'Precio', 
            'tamanio': 'Tamanio',
        }
        widgets={
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un codigo', 
                    'id': 'patente'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un nombre', 
                    'id': 'marca'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un precio', 
                    'id': 'modelo'
                }
            ), 
            'tamanio': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tamanio',
                }
            )
            

        }


 