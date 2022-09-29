from django.contrib import admin
from gestionPedidos.models import cliente, articulo, pedido

# Register your models here.

class clienteAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","mail") #este muestra en el panel lo seleccionado 
    search_fields=("nombre", "mail") #este es para crear una ventana de búsquedas en el panel

class articuloAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion", "precio")
    list_filter=("seccion",)#crea un filtro para busqueda por seccion

class pedidoAdmin(admin.ModelAdmin):
    list_display=("fecha",)
    date_hierarchy="fecha"#crea un filtro pequeño arriba por fecha

admin.site.register(cliente, clienteAdmin)
admin.site.register(articulo, articuloAdmin)
admin.site.register(pedido, pedidoAdmin)