from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse("Hello!")
    # Como retornar uam página externa
    # busca a página index dentro do diretório hello dos templates
    return render(request, "hello/index.html")

def joao(request):
    return HttpResponse("Hello, joao")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    # terceiro parametro é um dict
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })