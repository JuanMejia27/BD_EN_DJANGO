from django.shortcuts import render
from datetime import *

# Create your views here.
'''def home(request):
    context = {
        'name': 'Estudiante',
        'date': date.today(),
        'tasks': ['Estudiar', 'Practicar', 'Revisar ejercicios', 'Correr']
    }
    return render(request, 'index.html', context)'''

def dashboard(request):
    users = [
        {'name': 'Ana', 'correo': 'ana@example.com', 'joined': '2025-01-15'},
        {'name': 'Esli', 'correo': 'esli@example.com', 'joined': '202-01-15'},
        {'name': 'Jose', 'correo': 'jose@example.com', 'joined': '2022-01-15'},
    ]
    # pasar la lista de usuarios dentro de un diccionario
    context = {'users': users}
    return render(request, 'index.html', context)