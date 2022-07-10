from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import \
    HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


# Create your views here.
def index(request: object) -> object:
    return TemplateResponse(request, "carapp\\home.html")
    # header = "Персональні дані" #Звичайна змінна
    # langs = ["Англійська","Німецька","Іспанська"], #масив
    # user = {"name":"Ярослав","age":26} # словник
    # addr = ("Каунаська", 13, 2) # Кортеж
    # data={"header":header, "langs":langs, "user":user,"address":addr}
    # return TemplateResponse(request, "carapp\\index_app1.html", context=data)


def about(request: object) -> object:
    return HttpResponse("<h1>Про нас</h1>")


def contacts(request: object) -> object:
    return HttpResponse("<h1>Контакти</h1>")


def users1(request: object, id: int = 1, name: str = "Олександр") -> object:
    output = "<h2>Користувач:</h2><h3>id: {0} Ім'я: {1}</h3>".format(id, name)
    return HttpResponse(output)


def products(request: object, productid: int = 1) -> object:
    cat = request.GET.get("cat", "")
    output = "<h2>Товар №{0}</h2><br>Категорія: {1}".format(productid, cat)
    return HttpResponse(output)


def users(request: object) -> object:
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Олександр")
    output = "<h2>Користувач:</h2><h3>id: {0} Ім'я: {1}</h3>".format(id, name)
    return HttpResponse(output)


def personas(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")