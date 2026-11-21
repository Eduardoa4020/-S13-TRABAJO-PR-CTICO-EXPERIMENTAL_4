import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from core.models import Estudiante, Curso, Inscripcion


@login_required
def indice(request):
    return render(request, 'reportes/index.html')


@login_required
def estudiantes_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="estudiantes.csv"'
    response.write('\ufeff')
    writer = csv.writer(response)
    writer.writerow(['Matricula', 'Nombre', 'Email', 'Activo'])
    for estudiante in Estudiante.objects.all():
        writer.writerow([estudiante.matricula, estudiante.nombre, estudiante.email, estudiante.activo])
    return response


@login_required
def estudiantes_imprimir(request):
    return render(request, 'reportes/estudiantes_imprimir.html', {
        'estudiantes': Estudiante.objects.all(),
        'cursos': Curso.objects.count(),
        'inscripciones': Inscripcion.objects.count(),
    })
