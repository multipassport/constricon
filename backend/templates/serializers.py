from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField
from templates.models import Item, Pack, Part, Template


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        exclude = ['template']


class TemplateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class TemplateRetrieveSerializer(serializers.ModelSerializer):
    parts = PartSerializer(many=True)

    class Meta:
        model = Template
        fields = '__all__'


class PackSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Pack
        fields = '__all__'


class ItemSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Item
        fields = '__all__'
