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
    url(r'^events/$', event_view, name='event_view'),
    url(r'^certificates/$', certificate_view, name='certificate_view'),
    url(r'^partners/$', partner_view, name='partner_view'),
    url(r'^special_offers/$', special_offers, name='special_offers'),
    url(r'^kitchen/$', kitchen_view, name='kitchen_view'),
    url(r'^all_services/$', all_service_view, name='all_service_view'),
]
