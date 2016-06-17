from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
import serializers
from rest_framework import generics

import json
import urllib

# For orders_test only
from datetime import datetime
from django.template.loader import get_template
from pytz import timezone
import uuid
import requests

from catalog.models import *
from venue.models import *

def home(request):
    return render(request,
                  template_name='cashman/home.html')


def search(request):
    return render(request,
                  template_name='search.html')


def photos(request):
    return render(request,
                  template_name='photos.html')


def doUpload(request):
    if request.POST:
        if request.FILES == None:
            raise Http404("No files uploaded")
        f = request.FILES['file']        
        i = Images(image = request.FILES['file'])
        i.save()

    return displayAll(request)

def displayAll(request):
    images = Images.objects.all()
    categories = Category.objects.all()
    return render(request, 'cashman/displayAll.html',{'images':images,'categories':categories})

def searchPhotos(request):
    images = Images.objects.all()
    categories = Category.objects.all()
    return render(request, 'cashman/searchPhotos.html',{'photos':images,'categories':categories})

class ImageListAPIView(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = serializers.ImageListSerializer

class ImageAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = serializers.ImageSerializer

@api_view(('GET',))
def api_root(request, format = None):
    return Response({
        'images' : reverse('images',request = request, format = format),
    })
