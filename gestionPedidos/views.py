from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulo
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.


def busqueda_productos(request):  #aca se define una funcion para crear una pagina de busqueda de un producto

    return render(request, "busqueda_productos.html")

def buscar(request):  #aca se crea esta funcion para devolver la busqueda con el mensaje guardado en la variable mensaje de la busqueda_producto.html

    if request.GET["prd"]:


        #mensaje="Artículo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]
        if len(producto)>20:

            mensaje="Texto de búsqueda demasiado largo"

        else:

            articulos=articulo.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busquedas.html", {"articulos":articulos, "query":producto})

    else:
        mensaje="No has introducido un búsqueda válida. Favor de intentar nuevamente"

    return HttpResponse(mensaje)

## en las siguientes lineas de codigo, se crea una funcion para poder  enviar correos electronicos automaticos
# revisar en setting.py y en views.py para obtener mas ayuda de la creacion de estos paramteros.
def contacto(request):

    if request.method=="POST":

        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email',''),['tomas.prueba.stuardo@gmail.com'],)

            return render(request, "gracias.html")
    
    else:

        #Este formulario se puede hacer con una api form o crearlo directamente

        miFormulario=FormularioContacto()

    return render(request, "formulario_contacto.html", {"form":miFormulario})


        #subject=request.POST["asunto"]

        #mensajes=request.POST["mensaje"] + " " + request.POST["email"]

       # email_from=settings.EMAIL_HOST_USER

        #recibiendo_list=["tomas.prueba.stuardo@gmail.com"]

        #send_mail(subject, mensajes, email_from, recibiendo_list)

        #return render (request, "gracias.html")

    #else:
      #  mensaje="No ha sido posible enviar su mensaje"

    #return render (request, "contacto.html")