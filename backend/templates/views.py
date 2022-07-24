from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from templates import serializers
from templates.models import Item, Pack, Template


class TemplateListView(generics.ListAPIView):
    serializer_class = serializers.TemplateListSerializer
    queryset = Template.objects.all()


class TemplateRetrieveView(generics.RetrieveAPIView):
    serializer_class = serializers.TemplateRetrieveSerializer
    queryset = Template.objects.all()


class PackListView(generics.ListAPIView):
    serializer_class = serializers.PackSerializer
    queryset = Pack.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['tags']
    filterset_fields = {'colour': ['exact']}


class ItemListView(generics.ListAPIView):
    serializer_class = serializers.ItemSerializer
    queryset = Item.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['tags']
    filterset_fields = {'packs': ['exact']}


class ItemRetrieveView(generics.RetrieveAPIView):
    serializer_class = serializers.ItemSerializer
    queryset = Item.objects.all()
