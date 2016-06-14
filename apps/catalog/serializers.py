from rest_framework import serializers
from catalog.models import *

class ImageSerializer(serializers.Serializer):
	pass

	class Meta:
		model = Images