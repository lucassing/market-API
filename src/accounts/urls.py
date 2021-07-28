from rest_framework import routers
from .views import TokenAPI, UserViewSet
from django.urls import path


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('token-auth/', TokenAPI.as_view(), name='api_token_auth'),
]

urlpatterns += router.urls
