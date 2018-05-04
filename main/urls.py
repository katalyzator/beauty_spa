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
    url(r'^service/(?P<slug>[\w-]+)/$', service_view, name='service_view'),
    url(r'^etiket/$', eticket_view, name='etiket_view'),
    url(r'^events/$', event_view, name='event_view'),
    url(r'^certificates/$', certificate_view, name='certificate_view'),
    url(r'^partners/$', partner_view, name='partner_view'),
    url(r'^special_offers/$', special_offers, name='special_offers'),
    url(r'^kitchen/$', kitchen_view, name='kitchen_view'),
    url(r'^all_services/$', all_service_view, name='all_service_view'),
    url(r'^post_application/$', post_application, name='post_application'),
    url(r'^news/(?P<id>\d+)/$', news_detail_view, name='single_news'),
    url(r'^pressa/(?P<id>\d+)/$', press_detail_view, name='single_press'),
    url(r'^publications/(?P<id>\d+)/$', publick_detail_view, name='single_public'),
    url(r'^event/(?P<id>\d+)/$', event_detail_view, name='single_event'),
    url(r'^cert/(?P<id>\d+)/$', cert_detail_view, name='single_cert'),
    url(r'^card/(?P<id>\d+)/$', card_detail_view, name='single_card'),
]
