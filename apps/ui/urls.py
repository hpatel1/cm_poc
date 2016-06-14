from django.conf.urls import patterns, include, url
from ui import views

urlpatterns = patterns('',
	                  url(r'^$',views.home,name = "cashman_home"),
	                  url(r'^doUpload/$',views.doUpload, name="file upload"),
	                  url(r'^displayAll/$', views.displayAll, name="display all")
                      # url(r'^$', views.home, name="cashman_home"),
                      # url(r'^search/$', views.search, name="cashman_search"),
                      # url(r'^photos/$', views.photos, name="cashman_photos"),
                      # url(r'^order-test/$', views.orders_test, name="orders_test"),
                      # url(r'^product/$', views.products, name="cashman_products"),
)
