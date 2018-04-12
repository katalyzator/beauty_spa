from django.conf.urls import url

from main.views import index_view, about_view, gallery_view, bootick_view, license_view

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^about/$', about_view, name='about_view'),
    url(r'^gallery/$', gallery_view, name='gallery_view'),
    url(r'^bootick/$', bootick_view, name='bootick_view'),
    url(r'^licenses/$', license_view, name='license_view'),
]
