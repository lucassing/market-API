from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from ..models import Category, Product, Basket, ItemBasket
from django.contrib.auth import get_user_model

User = get_user_model()


class BasketAPITest(APITestCase):
    user_credentials = {'username': 'testingUser',
                        'password': 'testingPassword',
                        'email': 'lucas@gmail.com', 'is_staff': True}
    category_data = {'name': 'Electronic'}

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(**cls.user_credentials)
        cls.basket = Basket.objects.create(user=cls.user)
        cls.category = Category.objects.create(**cls.category_data)

        cls.product1_data = {"name": "Iphone X",
                             "image": "https://www.google.com", "stock": "15",
                             "description": 'some description',
                             "price": "1999.99", "category": cls.category,
                             "creator": cls.user}

        cls.product2_data = {"name": "Dell Vostro",
                             "image": "https://www.apple.com", "stock": "5",
                             "description": 'some descr 2', "price": "999.99",
                             "category": cls.category, "creator": cls.user}

        cls.product1 = Product.objects.create(**cls.product1_data)
        cls.product2 = Product.objects.create(**cls.product2_data)

    def setUp(self) -> None:
        self.client.force_authenticate(user=self.user)

    def test_get_basket_ok_HTTP200(self):
        ItemBasket.objects.create(basket=self.basket,
                                  product=self.product1,
                                  qty=2)
        ItemBasket.objects.create(basket=self.basket,
                                  product=self.product2,
                                  qty=2)
        url = reverse('itemBasketList')
        response = self.client.get(url)
        self.assertEqual(len(response.data[0]['items']), 2)
        self.assertTrue(status.HTTP_200_OK, response.status_code)

    def test_add_product_to_basket_ok_HTTP201(self):
        """
        Test add a product to the basket
        :return:
        """
        url = reverse('addItemToBasket')
        request_data = {'product': self.product1.id, 'qty': 5}
        response = self.client.post(url, request_data)
        self.assertDictContainsSubset(request_data, response.data)
        self.assertTrue(status.HTTP_201_CREATED, response.status_code)

    def test_empty_product_field_fail_HTTP400(self):
        """
        Test fail adding a null product to the basket
        :return:
        """
        url = reverse('addItemToBasket')
        request_data = {'product': '', 'qty': 5}
        response = self.client.post(url, request_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_empty_qty_field_fail_HTTP400(self):
        """
        Test fail adding a null product to the basket
        :return:
        """
        url = reverse('addItemToBasket')
        request_data = {'product': self.product1.id, 'qty': ''}
        response = self.client.post(url, request_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_adding_no_authorized_fail_HTTP401(self):
        """
        Test fail adding a null product to the basket
        :return:
        """
        self.client.force_authenticate(user=None)
        url = reverse('addItemToBasket')
        request_data = {'product': self.product1.id, 'qty': 5}
        response = self.client.post(url, request_data)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_adding_no_existing_product_fail_HTTP400(self):
        """
        Test fail adding a null product to the basket
        :return:
        """
        url = reverse('addItemToBasket')
        request_data = {'product': "99999", 'qty': 5}
        response = self.client.post(url, request_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_set_0_qty_fail_HTTP400(self):
        """
        Test fail adding a null product to the basket
        :return:
        """
        url = reverse('addItemToBasket')
        request_data = {'product': self.product1.id, 'qty': 0}
        response = self.client.post(url, request_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_add_more_qty_than_in_stock_fail_HTTP400(self):
        """
        Test fail adding a null product to the basket
        :return:
        """
        url = reverse('addItemToBasket')
        request_data = {'product': int(self.product1.stock) + 5, 'qty': 0}
        response = self.client.post(url, request_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

