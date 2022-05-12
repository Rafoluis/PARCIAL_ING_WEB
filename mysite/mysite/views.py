from django.http import HttpResponse
def saludo(request): #vista
    return HttpResponse("Hola soy Rafael Corzo")