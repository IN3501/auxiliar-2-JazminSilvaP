from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def pestaña(request):
	return render(request, 'miapp/pestaña.html')

def equipo_docente(request):
	return render(request, 'miapp/equipo_docente.html')
	
