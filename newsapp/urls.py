from django.urls import path, re_path, register_converter
from newsapp.views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
     path('', index, name='home'),
     # path('s', shell),

]




# handler404 = PageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)