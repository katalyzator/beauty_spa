# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import Member, Review

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


admin.site.register(Review, ReviewAdmin)
admin.site.register(Member, MemberAdmin)
