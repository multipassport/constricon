from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'public_name',
            'avatar',
            'league',
        ]
        extra_kwargs = {
            'email': {'read_only': True},
            'public_name': {'required': False},
            'avatar': {'required': False},
            'league': {'required': False},
        }
