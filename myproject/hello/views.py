from django.shortcuts import render
 
def index(request):
    context = {"osoite": "Kaartokatu 2, 11100 Riihimäki"}
    return render(request, 'hello/index.html', context)