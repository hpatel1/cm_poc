from django.conf.urls import patterns, include, url
from catalog import views

urlpatterns = [
    url(r'^images/', views.ImagesView.as_view(), name="images"),
    url(r'^set-category/', views.set_category, name="set_category"),
]
