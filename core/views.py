from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CursoForm, EstudianteForm
from .models import Curso, Estudiante, Inscripcion


@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html', {
        'total_estudiantes': Estudiante.objects.count(),
        'total_cursos': Curso.objects.count(),
        'total_inscripciones': Inscripcion.objects.count(),
    })


@login_required
def estudiante_list(request):
    return render(request, 'core/estudiantes/list.html', {'estudiantes': Estudiante.objects.all()})


@login_required
def estudiante_create(request):
    return estudiante_form(request, EstudianteForm(), 'Estudiante creado.')


@login_required
def estudiante_update(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return estudiante_form(request, EstudianteForm(instance=estudiante), 'Estudiante actualizado.', estudiante)


def estudiante_form(request, form, success_message, estudiante=None):
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect('estudiante_list')
    return render(request, 'core/estudiantes/form.html', {'form': form, 'objeto': estudiante})


@login_required
def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        messages.success(request, 'Estudiante eliminado.')
        return redirect('estudiante_list')
    return render(request, 'core/confirm_delete.html', {'objeto': estudiante})


@login_required
def curso_list(request):
    return render(request, 'core/cursos/list.html', {'cursos': Curso.objects.all()})


@login_required
def curso_create(request):
    return curso_form(request, CursoForm(), 'Curso creado.')


@login_required
def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return curso_form(request, CursoForm(instance=curso), 'Curso actualizado.', curso)


def curso_form(request, form, success_message, curso=None):
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect('curso_list')
    return render(request, 'core/cursos/form.html', {'form': form, 'objeto': curso})


@login_required
def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado.')
        return redirect('curso_list')
    return render(request, 'core/confirm_delete.html', {'objeto': curso})
