from django.shortcuts import render
from django.http import HttpResponse
#from django.template import Template,Context
from bs4 import BeautifulSoup
import json
import requests 
#Request: Para realizar peticiones
#HttpResponse: para enviar una respuesta usando protocolo http 
def tracked_product(tracked_product):
        product_list=[]
        for i in tracked_product:
            product_elements = i.split('*')
            product_list.append({
                'Title':product_elements[1],
                'ID':product_elements[0],
                'Score':float(product_elements[2]),
                'Price':float(product_elements[3]),
                'Image':product_elements[4]
            })  
        return product_list
def miPrimeraPlantilla1(request):
    roger={'name':"roger"}
    result = requests.post("http://127.0.0.1:5600/backend/roger")#aqui se concatena el producto a buscar como añadir un body a una peticion get 
    list_of_frontend=BeautifulSoup(result.content, 'html.parser')
    return HttpResponse(list_of_frontend)
def frontend(request):
    #print (search_input)
    if request.method == 'POST':
        if "search_btn" in request.POST:
            search_input = request.POST["input-product"]
            if not search_input == "":
                result = requests.get(f"http://127.0.0.1:5600/backend/{search_input}")
                global list_of_frontend
                list_of_frontend=json.loads(result.content)
                print (type(list_of_frontend))
                return render(request , "main.html", {"product":list_of_frontend})
        
        elif "track_btn" in request.POST:
            product_track = request.POST.getlist("products")
            product_tracked = tracked_product(product_track)
            print (list_of_frontend)
            return render(request, "main.html",{"product":list_of_frontend,"product_tracked":product_tracked})
    return render(request , "main.html")