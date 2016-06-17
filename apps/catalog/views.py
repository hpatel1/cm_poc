from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, ValidationError
from serializers import *
from catalog.models import Images
from cashman.generics import GenericView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from rest_framework.views import APIView


class ImagesView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Images.objects.all()
    api_view = ['POST', 'GET']

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'stat':'success'}, status=status.HTTP_200_OK)

    def get_object(self):
        if self.request.method == 'GET':
            id = self.request.query_params.get('id', None)
        else:
            id = self.request.data.get('id',None)
        try:
            return Images.objects.get(id=id)
        except Images.DoesNotExist:
            raise NotFound("Requested image is not found")


class SetCategory(APIView):
    serializer_class = ImageSerializer
    queryset = Images.objects.all()
    api_view = ['POST', 'GET']

    def post(self, request):
        return self.set_category(request)

    def set_category(self, request):
        if request.data.get('category', None):
            try:
                category = Category.objects.get(id=request.data['category'])
            except Category.DoesNotExist as exception:
                raise NotFound("Requested category is not found.")
        else:
            raise NotFound("Please provide valid category id")

        if request.data.get('images', None):
            for image in Images.objects.filter(id__in = request.POST['images'].split(',')):
                image.category = category
                image.save()
            return Response({'stat':'success'}, status=status.HTTP_200_OK)
        else:
            raise NotFound("No images are found.")

set_category = SetCategory.as_view()
