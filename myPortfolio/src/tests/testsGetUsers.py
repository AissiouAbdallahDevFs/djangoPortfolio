import os
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from dotenv import load_dotenv
from colorama import init, Fore

init(autoreset=True)

class UserViewSetTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        super().setUpClass()

    def setUp(self):
        username = os.environ.get('TEST_USERNAME')
        password = os.environ.get('TEST_PASSWORD')
        self.user = User.objects.create_user(username=username, password=password)


    def test_list_users_authenticated(self):
        username = os.environ.get('TEST_USERNAME')
        password = os.environ.get('TEST_PASSWORD')
        self.client.login(username=username, password=password)
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(Fore.GREEN + "Le test test_list_users_authenticated a réussi ! 🚀🚀🚀")

    def test_list_users_unauthenticated(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print(Fore.GREEN + "Le test test_list_users_unauthenticated a réussi ! 🚀🚀🚀")
