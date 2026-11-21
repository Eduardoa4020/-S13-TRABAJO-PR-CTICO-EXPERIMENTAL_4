from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Estudiante, Curso, Inscripcion


@login_required
def indice(request):
    estudiantes_nuevos = Estudiante.objects.filter(activo=True).count()
    cursos_activos = Curso.objects.filter(activo=True).count()
    inscripciones = Inscripcion.objects.count()
    return render(request, 'notificaciones/index.html', {
        'items': [
            f'{estudiantes_nuevos} estudiantes activos',
            f'{cursos_activos} cursos activos',
            f'{inscripciones} inscripciones registradas',
        ],
    })
