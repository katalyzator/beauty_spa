# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import Member

admin.site.site_header = 'Панель управления Beauty Spa'


class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'profession']

    class Meta:
        model = Member


admin.site.register(Member, MemberAdmin)
