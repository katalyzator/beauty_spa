# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from main.models import Member


def index_view(request):
    members = Member.objects.all()
    context = {
        "members": members
    }
    template = 'index.html'

    return render(request, template, context)


def about_view(request):
    context = {}
    template = 'abou_us.html'

    return render(request, template, context)


def gallery_view(request):
    context = {}
    template = 'gallery-page.html'

    return render(request, template, context)


def bootick_view(request):
    context = {}
    template = 'bootick.html'

    return render(request, template, context)


def license_view(request):
    context = {}
    template = 'license.html'

    return render(request, template, context)