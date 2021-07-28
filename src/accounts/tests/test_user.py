from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from accounts.views import UserViewSet
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist


class UserTestCase(APITestCase):
    test_user = None
    user_credentials = {'username': 'testingUser',
                        'password': 'testingPassword'}

    @classmethod
    def setUpTestData(cls):
        cls.test_user = get_user_model().objects.create(**cls.user_credentials)

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_create_user(self):
        """
        Test new user creation endpoint.
        """
        new_user_data = {'username': 'lucassing',
                         'password': '123456',
                         'email': 'lucas@gmail.com'}

        url = reverse('user-list')
        request = self.factory.post(url, new_user_data)
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)

        password = new_user_data.pop('password')

        self.assertTrue(check_password(password, response.data.get('password')))
        self.assertDictContainsSubset(new_user_data, response.data)
        self.assertTrue(status.is_success(response.status_code))

    def test_get_user(self):
        """
        Test get user information method.
        """
        url = reverse('user-detail', kwargs={'pk': self.test_user.id})
        request = self.factory.get(url)
        view = UserViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.test_user.id)

        self.assertDictContainsSubset(self.user_credentials, response.data)
        self.assertTrue(status.is_success(response.status_code))

    def test_modify_username(self):
        """
        Test user mutation method.
        """
        new_username = 'lucasModified'
        url = reverse('user-detail', kwargs={'pk': self.test_user.id})
        request = self.factory.put(url, {'username': new_username})

        view = UserViewSet.as_view({'put': 'partial_update'})
        response = view(request, pk=self.test_user.id)

        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data.get('username'), new_username)

    def test_destroy_user(self):
        """
        Test user destroy method.
        """
        url = reverse('user-detail', kwargs={'pk': self.test_user.id})
        request = self.factory.delete(url)
        view = UserViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.test_user.id)

        with self.assertRaises(ObjectDoesNotExist):
            get_user_model().objects.get(id=self.test_user.id)
        self.assertTrue(status.is_success(response.status_code))
