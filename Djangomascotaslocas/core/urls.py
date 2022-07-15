from django.contrib import admin
from django.urls import path
from core.views import home, quienessomos, galeriadefotos, formularioderegistro, comentario, administracion, form_crear_cliente, form_crear_producto,form_mod_cliente,form_mod_producto, form_del_cliente, form_del_producto, tienda,agregar_producto,eliminar_producto,restar_producto,limpiar_carrito

urlpatterns=[
    path('', home, name="home"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('galeriadefotos/', galeriadefotos, name="galeriadefotos"),
    path('formularioderegistro/', formularioderegistro, name="formularioderegistro"),
    path('comentario/', comentario, name="comentario"),
    path('administracion/', administracion, name="administracion"),
    path('form_crear_cliente/', form_crear_cliente, name="form_crear_cliente"),
    path('form_crear_producto/', form_crear_producto, name="form_crear_producto"),
    path('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
    path('tienda/', tienda, name="tienda"),
    path('agregar/<producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<producto_id>/', eliminar_producto, name="Del"),
    path('restar/<producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

]