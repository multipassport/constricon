from django_filters.rest_framework import DjangoFilterBackend
from icons import serializers
from icons.models import Icon, IconPart
from rest_framework import generics
from rest_framework.filters import SearchFilter


class IconListCreateView(generics.ListCreateAPIView):
    queryset = Icon.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['tags']
    filterset_fields = {'user': ['exact']}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.IconCreateSerializer
        return serializers.IconListSerializer


class IconRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Icon.objects.all()
    http_method_names = ['put', 'get', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return serializers.IconUpdateSerializer
        return serializers.IconRetrieveSerializer


class IconPartUpdateView(generics.UpdateAPIView):
    queryset = IconPart.objects.all()
    serializer_class = serializers.IconPartSerializer
    http_method_names = ['put']
