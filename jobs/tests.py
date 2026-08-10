from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from jobs.models import JobApplication
from datetime import date

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def get_token(self):
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        }, format='json')
        return response.data['access']

    def test_register(self):
        response = self.client.post('/api/auth/register/', {
            'username': 'newuser',
            'email': 'new@test.com',
            'password': 'newpass123'
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)

    def test_login_wrong_password(self):
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'wrongpass'
        }, format='json')
        self.assertEqual(response.status_code, 401)

class JobApplicationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        }, format='json')
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        self.job = JobApplication.objects.create(
            user=self.user,
            company='SAP SE',
            role='Python Developer',
            location='Munich',
            job_type='full-time',
            status='applied',
            applied_date=date.today()
        )

    def test_create_application(self):
        response = self.client.post('/api/applications/', {
            'company': 'Siemens',
            'role': 'Backend Developer',
            'location': 'Berlin',
            'job_type': 'full-time',
            'status': 'applied',
            'applied_date': '2026-08-06'
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['company'], 'Siemens')

    def test_list_applications(self):
        response = self.client.get('/api/applications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_delete_application(self):
        response = self.client.delete(f'/api/applications/{self.job.id}/')
        self.assertEqual(response.status_code, 204)

    def test_update_status(self):
        response = self.client.patch(f'/api/applications/{self.job.id}/', {
            'status': 'interview',
            'company': self.job.company,
            'role': self.job.role,
            'job_type': self.job.job_type,
            'applied_date': str(self.job.applied_date)
        }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'interview')

    def test_unauthenticated_access(self):
        self.client.credentials()
        response = self.client.get('/api/applications/')
        self.assertEqual(response.status_code, 401)

    def test_dashboard_stats(self):
        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('total', response.data)
        self.assertEqual(response.data['total'], 1)