from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from beauty_spa import settings
from main.views import ajax_member_detail_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ajax_member_detail', ajax_member_detail_view, name='ajax_member_detail'),
    url(r'', include('main.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
