# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import *

admin.site.site_header = 'Панель управления Beauty Spa'


class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'profession']

    class Meta:
        model = Member


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'is_active']
    list_editable = ['is_active']

    class Meta:
        model = Review


class DiscountCertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']

    class Meta:
        model = DiscountCertificate


class DiscountCardAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']

    class Meta:
        model = DiscountCard


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

    class Meta:
        model = Service


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Partner


class GalleryAdmin(admin.ModelAdmin):
    class Meta:
        model = Gallery


class LicenseAdmin(admin.ModelAdmin):
    class Meta:
        model = License


class SliderAdmin(admin.ModelAdmin):
    class Meta:
        model = Slider


class BootickAdmin(admin.ModelAdmin):
    class Meta:
        model = Bootick


class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event


class NewsAdmin(admin.ModelAdmin):
    class Meta:
        model = News


class PublicationAdmin(admin.ModelAdmin):
    class Meta:
        model = Publication


class PressAdmin(admin.ModelAdmin):
    class Meta:
        model = Press


class AboutAdmin(admin.ModelAdmin):
    class Meta:
        model = About


class PrincipeAdmin(admin.ModelAdmin):
    class Meta:
        model = Principe


admin.site.register(Principe, PrincipeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Press, PressAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Bootick, BootickAdmin)
admin.site.register(Application)
admin.site.register(Slider, SliderAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(DiscountCard, DiscountCardAdmin)
admin.site.register(DiscountCertificate, DiscountCertificateAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Member, MemberAdmin)
