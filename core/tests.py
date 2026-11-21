from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Curso, Estudiante


class CoreTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='demo', password='Demo12345!')

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_crud_estudiante(self):
        self.client.login(username='demo', password='Demo12345!')
        response = self.client.post(reverse('estudiante_create'), {
            'nombre': 'Ana Perez',
            'email': 'ana@example.com',
            'matricula': 'A001',
            'activo': 'on',
        })
        self.assertRedirects(response, reverse('estudiante_list'))
        self.assertTrue(Estudiante.objects.filter(matricula='A001').exists())

    def test_crud_curso(self):
        self.client.login(username='demo', password='Demo12345!')
        response = self.client.post(reverse('curso_create'), {
            'nombre': 'Django',
            'codigo': 'DJ-101',
            'creditos': 3,
            'activo': 'on',
        })
        self.assertRedirects(response, reverse('curso_list'))
        self.assertTrue(Curso.objects.filter(codigo='DJ-101').exists())
