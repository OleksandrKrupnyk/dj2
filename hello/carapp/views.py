from django.template.response import TemplateResponse
from django.http import \
    HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> object:
    # return TemplateResponse(request, "carapp\\home.html")
    cat = [
        {"title":"Ноутбуки", "link":"/#"},
        {"title":"Монітори", "link":"/#"},
        {"title":"Клавіатури", "link":"/#"},
        {"title":"Мишки", "link":"/#"},
        {"title":"Підставки", "link":"/#"},
           ]
    data = {"cat":cat}
    return render(request, "carapp\\index.html", context=data)
    # header = "Персональні дані" #Звичайна змінна
    # langs = ["Англійська","Німецька","Іспанська"], #масив
    # user = {"name":"Ярослав","age":26} # словник
    # addr = ("Каунаська", 13, 2) # Кортеж
    # data={"header":header, "langs":langs, "user":user,"address":addr}
    # return TemplateResponse(request, "carapp\\index_app1.html", context=data)


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Про нас</h1>")


def contacts(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Контакти</h1>")


def users1(request: HttpRequest, id: int = 1, name: str = "Олександр") -> HttpResponse:
    output = "<h2>Користувач:</h2><h3>id: {0} Ім'я: {1}</h3>".format(id, name)
    return HttpResponse(output)


def products(request: HttpRequest, productid: int = 1) -> HttpResponse:
    cat = request.GET.get("cat", "")
    output = "<h2>Товар №{0}</h2><br>Категорія: {1}".format(productid, cat)
    return HttpResponse(output)


def users(request: HttpRequest) -> HttpResponse:
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Олександр")
    output = "<h2>Користувач:</h2><h3>id: {0} Ім'я: {1}</h3>".format(id, name)
    return HttpResponse(output)


def personas(request: HttpRequest) -> HttpResponseRedirect:
    return HttpResponseRedirect("/about")


def details(request: HttpRequest) -> HttpResponsePermanentRedirect:
    return HttpResponsePermanentRedirect("/")