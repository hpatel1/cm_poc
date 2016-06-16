from rest_framework import serializers
from catalog.models import *
from versatileimagefield.serializers import VersatileImageFieldSerializer
from venue.serializers import CategorySerializer

class ImageSerializer(serializers.Serializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
    category = CategorySerializer()
    
    class Meta:
        model = Images
        fields = ['id', 'image', 'category']
