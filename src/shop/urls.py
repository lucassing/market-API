from django.urls import path
from .views import CategoryList, CategoryCreate, ProductList, \
    ProductCreate, ProductDetails

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categoryList'),
    path('categories/new/', CategoryCreate.as_view(), name='categoryCreate'),

    path('products/', ProductList.as_view(), name='productList'),
    path('products/new/', ProductCreate.as_view(), name='productCreate'),
    path('product/<int:id>/', ProductDetails.as_view(), name='productDetail'),
]
