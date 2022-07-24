from accounts import serializers
from django.contrib.auth import get_user_model
from rest_framework import generics


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.UserUpdateSerializer
    queryset = get_user_model()
    http_method_names = ['put']
