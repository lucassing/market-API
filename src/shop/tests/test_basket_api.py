from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from ..models import Category,Product, Basket, ItemBasket
from django.contrib.auth import get_user_model

User = get_user_model()


class BasketAPITest(APITestCase):
    user_credentials = {'username': 'testingUser',
                            'password': 'testingPassword',
                            'email': 'lucas@gmail.com',
                            'is_staff': True}
    category_data = {'name': 'Electronic'}

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(**cls.user_credentials)
        cls.category = Category.objects.create(**cls.category_data)

        cls.product1_data = {"name": "Iphone X",
                            "image": "https://www.google.com",
                            "stock": "15",
                            "description": 'some description',
                            "price": "1999.99",
                            "category": cls.category,
                            "creator": cls.user}

        cls.product2_data = {"name": "Dell Vostro",
                            "image": "https://www.apple.com",
                            "stock": "5",
                            "description": 'some descr 2',
                            "price": "999.99",
                            "category": cls.category,
                            "creator": cls.user}

        cls.product1 = Product.objects.create(**cls.product1_data)
        cls.product2 = Product.objects.create(**cls.product2_data)

    def setUp(self) -> None:
        self.client.force_authenticate(user=self.user)

    def test_add_product_to_basket(self):
        """
        Test add a product to the basket
        :return:
        """
        url = reverse('addItemToBasket')
        request_data = {'product': self.product1.id, 'qty': 5}
        response = self.client.post(url, request_data)
        self.assertDictContainsSubset(request_data, response.data)
        self.assertTrue(status.is_success(response.status_code))

    def test_fail_adding_empty_product_to_basket(self):
        """
        Test fail adding a null product to the basket
        :return:
        """
        url = reverse('addItemToBasket')
        request_data = {'product': '', 'qty': 5}
        response = self.client.post(url, request_data)
        self.assertTrue(status.is_client_error(response.status_code))

    def test_fail_adding_no_authorized(self):
        """
        Test fail adding a null product to the basket
        :return:
        """
        self.client.force_authenticate(user=None)
        url = reverse('addItemToBasket')
        request_data = {'product': self.product1.id, 'qty': 5}
        response = self.client.post(url, request_data)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_fail_adding_no_existing_product(self):
        """
        Test fail adding a null product to the basket
        :return:
        """
        url = reverse('addItemToBasket')
        request_data = {'product': "99999", 'qty': 5}
        response = self.client.post(url, request_data)
        self.assertTrue(status.is_client_error(response.status_code))


