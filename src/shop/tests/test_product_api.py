from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from ..models import Category, Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductAPITestCase(APITestCase):
    user_credentials = {'username': 'testingUser',
                        'password': 'testingPassword',
                        'email': 'lucas@gmail.com',
                        'is_staff': True}
    category_data = {'name': 'cell'}

    @classmethod
    def createUser(cls):
        return User.objects.create(**cls.user_credentials)

    @classmethod
    def createProduct(cls):
        return Product.objects.create(**cls.product_data)

    @classmethod
    def createCategory(cls):
        return Category.objects.create(**cls.category_data)

    @classmethod
    def setUpTestData(cls):
        cls.user = cls.createUser()
        cls.category = cls.createCategory()
        cls.product_data = {"name": "Iphone X",
                            "image": "https://cdn.idealo.com/folder/Product/5738/7/5738781/s1_p"
                                     "roduktbild_gross_3/apple-iphone-x.jpg",
                            "stock": "15",
                            "description": 'The iPhone X display has rounded corners that follo'
                                           'w a beautiful curved design, and these corners are '
                                           'within a standard rectangle. When measured as a '
                                           'standard rectangular shape, the screen is 5.85 '
                                           'inches diagonally (actual viewable area is less).',
                            "price": "1999.99",
                            "category": cls.category,
                            "creator": cls.user}
        cls.product = cls.createProduct()

    def setUp(self) -> None:
        self.client.force_authenticate(user=self.user)

    def test_create_new_product(self):
        """
        Test new Product creation
        :return:
        """
        url = reverse('productCreate')
        response = self.client.post(url, {**self.product_data, "category": self.category.id})
        self.assertTrue(status.is_success(response.status_code))

    def test_get_product(self):
        """
        Test new Product creation
        :return:
        """
        url = reverse('productDetail', kwargs={'id': self.product.id})
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))

    def test_update_product(self):
        """
        Test Product mutation
        :return:
        """
        self.product_data.update({'name': 'Iphone 11'})
        url = reverse('productDetail', kwargs={'id': self.product.id})
        response = self.client.put(url, data= {**self.product_data, "category": self.category.id})
        self.assertTrue(status.is_success(response.status_code))

    def test_eliminate_product(self):
        """
        Test Product delete
        :return:
        """
        url = reverse('productDetail', kwargs={'id': self.product.id})
        response = self.client.delete(url)
        with self.assertRaises(ObjectDoesNotExist):
            Product.objects.get(id=self.product.id)
        self.assertTrue(status.is_success(response.status_code))

    def test_fail_unauthenticate_product_create(self):
        """
        Test response 401_UNAUTHORIZED when no credentials are provided
        :return:
        """
        self.client.force_authenticate(user=None)
        url = reverse('productCreate')
        response = self.client.post(url, {**self.product_data, "category": self.category.id})
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create_new_category(self):
        url = reverse('categoryCreate')
        response = self.client.post(url, {'name': 'Computer'})
        self.assertTrue(status.is_success(response.status_code))

    def test_fail_create_existing_category(self):
        """
        Tests that the creation of a category fails when trying to create an existing one.
        :return:
        """
        url = reverse('categoryCreate')
        response = self.client.post(url, self.category_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
