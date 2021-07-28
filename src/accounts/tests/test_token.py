from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.reverse import reverse
from accounts.views import TokenAPI
from rest_framework import status
from accounts.serializers import UserSerializer


class TokenAPITestCase(APITestCase):
    test_user = None
    user_credentials = {'username': 'testingUser',
                        'password': 'testingPassword',
                        'email': 'lucas@gmail.com'}

    @classmethod
    def setUpTestData(cls):
        serializer = UserSerializer(data=cls.user_credentials)
        serializer.is_valid()
        cls.test_user = serializer.save()

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_create_new_token(self):
        """
        Test new Token creation
        :return:
        """
        url = reverse('api_token_auth')
        request = self.factory.post(url, self.user_credentials)
        view = TokenAPI.as_view()
        response = view(request)

        self.assertTrue(status.is_success(response.status_code))
        self.assertIn('token', response.data)
