from django.conf.urls import patterns, include, url
from django.contrib import admin
from cashman import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
import configurations
from ui.views import *

from ui import views as ui_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)


if 'api' in configurations.SERVER_TYPE:
    urlpatterns += patterns('',
#        url(r'^api/', include('api.urls')),
    )

urlpatterns += patterns('',
    url(r'^cashman/', include('ui.urls')),
    url(r'^doUpload/',doUpload, name="file upload"),
    url(r'^displayAll/', displayAll, name="display all"),
    url(r'^$', RedirectView.as_view(url='/cashman'), name='go-to-cashman'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

# urlpatterns += [
# 	url(r'^api/',
# 		include([
# 			url(r'^catalog/', include('catalog.urls')),
# 			url(r'^venue/', include('venue.urls')),
# 		], namespace='rest_apis')
# 	),
# ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)