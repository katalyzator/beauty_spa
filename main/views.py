# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from main.models import *

members = Member.objects.all()
gallery = Gallery.objects.all()
licenses = License.objects.all()
reviews = Review.objects.filter(is_active=True)
partners = Partner.objects.all()
services = Service.objects.all()
certificates = DiscountCertificate.objects.all()
cards = DiscountCard.objects.all()


def index_view(request):
    slider = Slider.objects.all()
    context = {
        "members": members,
        "reviews": reviews,
        "gallery": gallery,
        "sliders": slider
    }
    template = 'index.html'

    return render(request, template, context)


def about_view(request):
    context = {
        "members": members
    }
    template = 'abou_us.html'

    return render(request, template, context)


def gallery_view(request):
    context = {
        "gallery": gallery,
    }
    template = 'gallery-page.html'

    return render(request, template, context)


def bootick_view(request):
    context = {}
    template = 'bootick.html'

    return render(request, template, context)


def license_view(request):
    context = {
        "licenses": licenses
    }
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
    context = {
        "services": services
    }
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
    context = {
        "certificates": certificates,
        "cards": cards
    }
    template = 'spa-sertificat.html'

    return render(request, template, context)


def partner_view(request):
    context = {
        "partners": partners
    }
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


def all_service_view(request):
    context = {}
    template = 'all-service.html'

    return render(request, template, context)
