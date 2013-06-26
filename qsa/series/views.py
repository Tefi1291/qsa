# Create your views here.
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from series.forms import *
from series.models import *


def profile(request):
    """
        Vista que contiene toda la informacion del usuario
        Form para suscribirse a una serie
    """
    #user = request.user
    if request.method == "POST":
        form = SeriesForm(data=request.POST)
        # enviar pedido xml a tvdb
        # crear una serie en la base de datos

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mis_series.html')
    else:
        form = SeriesForm()
    return TemplateResponse(request, "home.html", {'form': form})


def about(request):
    ### Completar informacion sobre la pag. en about.html
    return TemplateResponse(request, "about.html")


def contact(request):
    """
        Informacion de contacto (administradores de la pag.)
    """
    return HttpResponseRedirect('/')