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


def information_view(request):
    context = {}
    template = 'information.html'

    return render(request, template, context)


def public_view(request):
    context = {}
    template = 'publick.html'

    return render(request, template, context)


def review_view(request):
    context = {}
    template = 'revius.html'

    return render(request, template, context)


def service_view(request):
    context = {}
    template = 'service.html'

    return render(request, template, context)


def eticket_view(request):
    context = {}
    template = 'etiket.html'

    return render(request, template, context)


def event_view(request):
    context = {}
    template = 'event.html'

    return render(request, template, context)


def certificate_view(request):
    context = {}
    template = 'spa-sertificat.html'

    return render(request, template, context)


def partner_view(request):
    context = {}
    template = 'partners.html'

    return render(request, template, context)


def special_offers(request):
    context = {}
    template = 'special-offers.html'

    return render(request, template, context)


def kitchen_view(request):
    context = {}
    template = 'spa_kitchen.html'

    return render(request, template, context)
