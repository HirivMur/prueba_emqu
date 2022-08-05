from django.test import TestCase
from rest_framework.test import APITestCase

from encuestas.views.encuestasViews import EncuestaCreateView
from .models import *
from rest_framework import status
from django.contrib.auth.models import User
import json
# Create your tests here.

class PostRedSocialTest(APITestCase):
    def setUp(self):

        self.json = {
            "descripcion": "Facebook"
        }

        self.user = User.objects.create_user(username='viridiana', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post('/api/encuestas/redsocial/create/', data=json.dumps(self.json), content_type="application/json")
        # print(f'response JSON ===>>> \n {json.dumps(response.data, cls=DecimalEncoder)} \n ---')
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class GetRedSocialTest(APITestCase):
    def setUp(self):
        RedesSocialesCatalogo.objects.create(descripcion='Facebook')
        RedesSocialesCatalogo.objects.create(descripcion='Instagram')
        RedesSocialesCatalogo.objects.create(descripcion='Tiktok')
        RedesSocialesCatalogo.objects.create(descripcion='Twitter')

        self.user = User.objects.create_user(username='viridiana', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/api/encuestas/redsocial/list/')
        print(f'response JSON ===>>> \n {json.dumps(response.json(), ensure_ascii=False)} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PutRedSocialTest(APITestCase):
    def setUp(self):
        RedesSocialesCatalogo.objects.create(id=1,descripcion='Facebook')
        RedesSocialesCatalogo.objects.create(id=2,descripcion='Instagram')
        RedesSocialesCatalogo.objects.create(id=3,descripcion='Tiktok')
        RedesSocialesCatalogo.objects.create(id=4,descripcion='Twitter')

        self.json = {
            "descripcion": "Facebook"
        }

        self.user = User.objects.create_user(username='viridiana', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.put('/api/encuestas/redsocial/1/update/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.data)} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
