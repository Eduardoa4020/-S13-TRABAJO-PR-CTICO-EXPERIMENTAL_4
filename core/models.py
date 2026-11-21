from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.matricula})'


class Curso(models.Model):
    nombre = models.CharField(max_length=120)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveSmallIntegerField(default=3)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'curso')
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.estudiante} -> {self.curso}'
