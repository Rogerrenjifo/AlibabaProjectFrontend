from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from bs4 import BeautifulSoup
import requests 
#Request: Para realizar peticiones
#HttpResponse: para enviar una respuesta usando protocolo http 

def miPrimeraPlantilla1(request):
    plantillaExterna= open("AlibabaProjectFrontend/templates/main.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close
    contexto= Context()#crar un contexto
    documento=template.render(contexto)
    return HttpResponse(documento)
def frontend(request):
    result = requests.get("http://127.0.0.1:5600/backend")
    list_of_frontend=BeautifulSoup(result.content, 'html.parser')
    return HttpResponse(list_of_frontend)
