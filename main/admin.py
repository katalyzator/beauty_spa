# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'profession']

    class Meta:
        model = Member


admin.site.register(Member, MemberAdmin)
