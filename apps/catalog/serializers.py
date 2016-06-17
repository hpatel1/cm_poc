from rest_framework import serializers
from catalog.models import *
from versatileimagefield.serializers import VersatileImageFieldSerializer
from venue.serializers import CategorySerializer
from cashman.serializers import DynamicModelSerializer

class ImageSerializer(DynamicModelSerializer):

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(ImageSerializer, self).__init__(many=many, *args, **kwargs)

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
        
    class Meta:
        model = Images
        fields = ['id', 'image', 'category']

    def update(self, instance, validated_data):
        return instance.update(
            image=validated_data.get('image', instance.image),
            category=validated_data.get('category', instance.category)
        )
