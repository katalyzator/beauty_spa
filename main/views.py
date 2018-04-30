# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from main.models import *

members = Member.objects.all()
gallery = Gallery.objects.all()
licenses = License.objects.all()
reviews = Review.objects.filter(is_active=True)
partners = Partner.objects.all()
# services = Service.objects.all()
certificates = DiscountCertificate.objects.all()
cards = DiscountCard.objects.all()


@csrf_exempt
def post_application(request):
    try:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        Application.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)

        return JsonResponse(dict(message="Success"))

    except:
        return HttpResponse(status=403)


def index_view(request):
    slider = Slider.objects.all()
    context = {
        "members": members,
        "reviews": reviews,
        "gallery": gallery,
        "sliders": slider,
        "partners": partners
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
    # for item in gallery:
    #     print item.type_of_gallery
    context = {
        "gallery": gallery,
    }
    template = 'gallery-page.html'

    return render(request, template, context)


def bootick_view(request):
    bootick = Bootick.objects.all()
    context = {"booticks": bootick}
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
    publics = Publication.objects.all()
    presses = Press.objects.all()
    context = {"publics": publics, "presses": presses}
    template = 'publick.html'

    return render(request, template, context)


def review_view(request):
    context = {"reviews": reviews}
    template = 'revius.html'

    return render(request, template, context)


def service_view(request, slug):
    services = Service.objects.filter(category=slug)

    page_title = ''

    if slug == 'consulting':
        page_title = "Диагностика и консультации"

    if slug == 'medicine':
        page_title = "Косметология и эстетическая медицина"

    if slug == 'spa':
        page_title = "SPA терапия"

    if slug == 'bath_spa':
        page_title = "Банный SPA"

    if slug == 'art_beauty':
        page_title = "Арт и Бьюти студия"

    context = {
        "services": services,
        "page_title": page_title
    }
    template = 'service.html'

    return render(request, template, context)


def eticket_view(request):
    context = {}
    template = 'etiket.html'

    return render(request, template, context)


def event_view(request):
    events = Event.objects.all()
    news = News.objects.all()
    context = {"events": events, "news": news}
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
