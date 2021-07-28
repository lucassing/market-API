from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """List, Create, Update, Retrieve, and Delete a user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TokenAPI(ObtainAuthToken):
    """Creates or retrieves the Token for a given user"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {'token': token.key, 'user_id': user.pk, 'email': user.email})
