#This Project with all app insite Created By: SUHAIB TAHA ALRIAH
#Email: alromys47@gmail.com
"""
Main setting urls
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include('geology.urls')),
    path('geo_dectionary/', include('dectionary.urls')), 
    path('profile/', include('provile.urls')), 
    path('ckeditor/', include('ckeditor_uploader.urls')), 

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
                        path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
                    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

