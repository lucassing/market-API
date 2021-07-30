from .serializers import CategorySerializer, ProductSerializer, \
    ItemBasketSerializer, BasketSerializer
from rest_framework.authentication import TokenAuthentication, \
    BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product, Basket, ItemBasket
from rest_framework import generics, status
from rest_framework.exceptions import NotFound


class CategoryCreate(generics.CreateAPIView):
    """Creates a category

    *
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryList(generics.ListAPIView):
    """List categories

    -
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(generics.ListAPIView):
    """Retrieves the list with all the products in the store.

    *
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(generics.CreateAPIView):
    """Creates a new Product

    **AUTHENTICATION REQUIRED**
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    """Retrieves, Update, Destroy Product

     **AUTHENTICATION REQUIRED**
     """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'id'
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class BasketItemCreate(generics.CreateAPIView):
    """Add a new item to the user's basket

     **AUTHENTICATION REQUIRED**
     """
    queryset = ItemBasket.objects.all()
    serializer_class = ItemBasketSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class BasketItemList(generics.ListAPIView):
    """List all items in the user's basket

     **AUTHENTICATION REQUIRED**
     """
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()


class BasketItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemBasket.objects.all()
    serializer_class = ItemBasketSerializer

