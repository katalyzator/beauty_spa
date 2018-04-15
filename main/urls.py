from django.conf.urls import url

from main.views import *

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^about/$', about_view, name='about_view'),
    url(r'^gallery/$', gallery_view, name='gallery_view'),
    url(r'^bootick/$', bootick_view, name='bootick_view'),
    url(r'^licenses/$', license_view, name='license_view'),
    url(r'^information/$', information_view, name='information_view'),
    url(r'^public/$', public_view, name='public_view'),
    url(r'^reviews/$', review_view, name='review_view'),
    url(r'^services/$', service_view, name='service_view'),
    url(r'^etiket/$', eticket_view, name='etiket_view'),
]
