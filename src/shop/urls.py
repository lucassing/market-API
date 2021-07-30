from django.urls import path
from .views import CategoryList, CategoryCreate, ProductList, \
    ProductCreate, ProductDetails, BasketItemCreate, BasketItemList, BasketItemDetails

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categoryList'),
    path('categories/new/', CategoryCreate.as_view(), name='categoryCreate'),

    path('products/', ProductList.as_view(), name='productList'),
    path('products/new/', ProductCreate.as_view(), name='productCreate'),
    path('product/<int:id>/', ProductDetails.as_view(), name='productDetail'),

    path('basket/add_item/', BasketItemCreate.as_view(),
         name='addItemToBasket'),
    path('basket/', BasketItemList.as_view(), name='itemBasketList'),
    path('basket/item/<int:id>/', BasketItemDetails.as_view(), name='itemBasketDetail'),
]
