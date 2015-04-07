from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Veraneo
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def lugares(request):
    lista = Veraneo.objects.all()
    salida = ""
    for fila in lista:
        salida += "<ul>\n"
        salida += fila.sitio
        salida += "</ul>\n"
    return HttpResponse(salida)


@csrf_exempt
def info(request, recurso):
    if request.method == "POST":
        lugar = Veraneo(sitio=request.POST['sitio'],
                        precio=request.POST['precio'],
                        duracion=request.POST['duracion'])
        lugar.save()  # guardar sitio en la base de datos
    elif request.method == "PUT":
        (sitio, precio, dias) = request.body.split(';')
        lugar = Veraneo(sitio=sitio, precio=precio, duracion=dias)
        lugar.save()  # guardar en la base de datos

    lista = Veraneo.objects.filter(sitio=recurso)  # recurso es el sitio
    salida = ""
    if not lista:  # si no esta en la lista se manda el formulario
        if request.user.is_authenticated():
            form = "<form action='' method='POST'>\n"
            form += "Lugar: <input type='text' name='sitio' value='" 
            form += recurso + "'><br>\n"
            form += "Precio: <input type='text' name='precio'><br>\n"
            form += "Duracion: <input type='text' name='duracion'><br>\n"
            form += "<input type='submit' value='enviar'>\n"
            form += "</form>\n"
        return HttpResponse(form)
    for fila in lista:
        salida += fila.sitio, str(fila.precio), str(fila.duracion)
    if request.user.is_authenticated():
        salida += "<br>" + request.user.username
        + " quieres hacer logout? <a href='/logout'>Logout</a>"
    else:
        salida += "No estas autenticado. <a"
        + "href='http://127.0.0.1:8000/admin/login/'>Haz login</a>"
    return HttpResponse(salida)


def notfound(request, recurso):
    return HttpResponseNotFound("No encontrado el recurso "
                                + recurso + "<ul>\n"
                                + "Pruebe con http://127.0.0.1:8000/sitio/"
                                + "(su destino)" + "</ul>\n")
