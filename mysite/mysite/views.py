from django.http import HttpResponse
def saludo(request): #vista
    return HttpResponse("Hola mundo soy Rafael Corzo")