from django.shortcuts import render
from rest_framework import generics
from serializers import *


class ImagesView(generics.ListCreateAPIView):
	serializer_class = ImageSerializer