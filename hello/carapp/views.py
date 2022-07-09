from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request: object) -> object:
    return HttpResponse("<h1>Головна</h1>")


def about(request: object) -> object:
    return HttpResponse("<h1>Про нас</h1>")


def contacts(request: object) -> object:
    return HttpResponse("<h1>Контакти</h1>")


def users(request: object, id: int=1, name: str="Олександр") -> object:
    output = "<h2>Користувач:</h2><h3>id: {0} Ім'я: {1}</h3>".format(id, name)
    return HttpResponse(output)


def products(request: object, productid: int = 1) -> object:
    output = "<h2>Товар №{0}</h2>".format(productid)
    return HttpResponse(output)