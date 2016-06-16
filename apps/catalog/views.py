from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import NotFound, ValidationError
from serializers import *
from catalog.models import Images


class ImagesView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Images.objects.all()

def set_category(request):
    if request.POST.get(category, None):
        try:
            category = Category.objects.get(id=request.POST['category'])
        except Category.DoesNotExist as exception:
            raise NotFound("Requested category is not found")
    else:
        raise NotFound("Requested category is not found")

    if request.POST.get(images, None):
        for image in Images.objects.filter(id__in = request.POST['images'].split(',')):
            image.category = category
            image.save()
    else:
        raise NotFound("No images are found.")

    return Response(status=status.HTTP_200_OK)
