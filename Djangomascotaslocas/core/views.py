from django.shortcuts import render, redirect
from .Carrito import Carrito
from .models import Cliente,Producto
from .forms import ClienteForm, ProductoForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def quienessomos(request):
    return render(request, 'quienessomos.html')

def galeriadefotos(request):
    return render(request, 'galeriadefotos.html')

def formularioderegistro(request):
    return render(request, 'formularioderegistro.html')

def comentario(request):
    return render(request, 'comentario.html')

#----- Mostrar los objetos almacenados de la clase cliente y producto -----#

def administracion(request):
    clientes  = Cliente.objects.all()
    productos = Producto.objects.all()

    datos= {
        'clientes'  : clientes,
        'productos' : productos
    }
    return render(request, 'administracion.html', datos)

#----- CLIENTE -----#

def form_crear_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid:
            cliente_form.save()
            return redirect('administracion')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form':cliente_form})

#----- PRODUCTO -----#

def form_crear_producto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid:
            producto_form.save()
            return redirect('administracion')
    else:
        producto_form = ProductoForm()
    return render(request, 'form_crear_producto.html', {'producto_form':producto_form})


#----- MODIFICAR UN OBJETO DE TIPO CLIENTE -----#
def form_mod_cliente(request,id):
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance=cliente)

    }
    if request.method=='POST':
        formulario=ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            return redirect('administracion')
    
    return render(request, 'form_mod_cliente.html' , datos)


#----- MODIFICAR UN OBJETO DE TIPO PRODUCTO -----#
def form_mod_producto(request,id):
    producto = Producto.objects.get(codigo=id)
    datos = {
        'form': ProductoForm(instance=producto)

    }
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect('administracion')
    
    return render(request, 'form_mod_producto.html' , datos)


#----- ELMINAR UN OBJETO DE TIPO CLIENTE -----#
def form_del_cliente(request,id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('administracion')


#----- ELMINAR UN OBJETO DE TIPO PRODUCTO -----#
def form_del_producto(request,id):
    producto = Producto.objects.get(codigo=id)
    producto.delete()
    return redirect('administracion')


#----- TIENDA DE PRODUCTOS -----#
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(codigo = producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(codigo =producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(codigo =producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")