from icons import serializers
from icons.models import Icon, IconPart
from rest_framework import generics


class IconListCreateView(generics.ListCreateAPIView):
    queryset = Icon.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.IconCreateSerializer
        return serializers.IconListSerializer


class IconRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Icon.objects.all()
    http_method_names = ['PUT', 'GET', 'DELETE']

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return serializers.IconUpdateSerializer
        return serializers.IconRetrieveSerializer


class IconPartUpdateView(generics.UpdateAPIView):
    queryset = IconPart.objects.all()
    serializer_class = serializers.IconPartSerializer
    http_method_names = ['PUT']
