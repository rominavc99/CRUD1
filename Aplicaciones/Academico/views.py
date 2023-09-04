from django.shortcuts import render, redirect
from . models import Curso

# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursos})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    
    # Verificar si el campo de casilla de verificación está presente y marcado
    activo = request.POST.get('chkDisponible') == 'true'

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, activo=activo)

    return redirect('/')





def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso":curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    
    activo = request.POST.get('chkDisponible') == 'on'  # Cambia a 'on' en lugar de 'true'

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.activo = activo
    curso.save()

    return redirect('/')

