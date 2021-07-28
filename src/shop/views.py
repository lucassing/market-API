from .serializers import CategorySerializer, ProductSerializer
from rest_framework.authentication import TokenAuthentication, \
    BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product
from rest_framework import generics


class CategoryCreate(generics.CreateAPIView):
    """
    Creates a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryList(generics.ListAPIView):
    """
    List categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(generics.ListAPIView):
    """
    Retrieves the list of products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(generics.CreateAPIView):
    """Creates a new Product
    AUTHENTICATION REQUIRED"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    """Retrieves, Update, Destroy Product
     AUTHENTICATION REQUIRED"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'id'
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
