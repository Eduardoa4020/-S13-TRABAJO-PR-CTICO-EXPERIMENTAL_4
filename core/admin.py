from django.contrib import admin
from .models import Curso, Estudiante, Inscripcion


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'email', 'activo')
    search_fields = ('nombre', 'matricula', 'email')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'creditos', 'activo')
    search_fields = ('codigo', 'nombre')


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha')
