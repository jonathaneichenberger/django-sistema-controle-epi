from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/pages/home.html')

def listar_epis(request):
    return render(request, 'core/pages/epis.html')

def usuarios(request):
    return render(request, 'core/pages/usuarios.html')

def entregas(request):
    return render(request, 'core/pages/entregas.html')

def relatorios(request):
    return render(request, 'core/pages/relatorios.html')

