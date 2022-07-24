from drf_writable_nested.serializers import WritableNestedModelSerializer
from icons.models import Icon, IconPart
from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField


class IconPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconPart
        exclude = ['icon']
        extra_kwargs = {
            'part': {'read_only': True},
        }


class IconCreateSerializer(TaggitSerializer, WritableNestedModelSerializer):
    tags = TagListSerializerField()
    icon_parts = IconPartSerializer(many=True)

    class Meta:
        model = Icon
        fields = '__all__'
        extra_kwargs = {
            'preview': {'read_only': True},
        }


class IconListSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Icon
        fields = '__all__'


class IconRetrieveSerializer(TaggitSerializer, serializers.ModelSerializer):
    icon_parts = IconPartSerializer(many=True)
    tags = TagListSerializerField()

    class Meta:
        model = Icon
        fields = '__all__'


class IconUpdateSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Icon
        fields = '__all__'
        extra_kwargs = {
            'template': {'read_only': True},
            'user': {'read_only': True},
        }
