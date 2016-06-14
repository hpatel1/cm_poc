from django.conf.urls import patterns, include, url
from catalog import views

urlpatterns = [
    url(r'^images/', views.ImagesView, name="images"),
]