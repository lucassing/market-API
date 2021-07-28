from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'is_staff']

    def create(self, validated_data):
        user = User(email=validated_data['email'],
            username=validated_data['username'],
            is_staff=validated_data['is_staff'], )
        user.set_password(validated_data['password'])
        user.save()
        return user
