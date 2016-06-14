from rest_framework import serializers
from catalog.models import *

class ImageListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Images
		view_name = 'image-detail'

class ImageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Images
		view_name = 'image-detail'


