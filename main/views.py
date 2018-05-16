# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

from main.models import *


# services = Service.objects.all()


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
    promotion = Promotion.objects.last()
    about = About.objects.last()
    reviews = Review.objects.filter(is_active=True)
    gallery = Gallery.objects.all()
    slider = Slider.objects.all()
    partners = Partner.objects.all()
    members = Member.objects.all()
    context = {
        "members": members,
        "reviews": reviews,
        "gallery": gallery,
        "sliders": slider,
        "partners": partners,
        "about": about,
        "promotion": promotion
    }
    template = 'index.html'

    return render(request, template, context)


def about_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='about').exists():
        page_image = PageImage.objects.filter(category='about').last()

    about = About.objects.last()
    members = Member.objects.all()
    principes = Principe.objects.all()
    context = {
        "members": members,
        "about": about,
        "principes": principes,
        "page_image": page_image
    }
    template = 'abou_us.html'

    return render(request, template, context)


def ajax_member_detail_view(request):
    member_id = request.GET.get('member_id')

    member = Member.objects.get(id=member_id)

    context = {
        "member": member
    }

    return render_to_response('partial/_member_detail.html', context)


def ajax_offer_view(request):
    offer_id = request.GET.get('offer_id')

    offer = SpecialOffer.objects.get(id=offer_id)

    context = {
        "offer": offer
    }

    return render_to_response('partial/_offer_detail.html', context)


def gallery_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='gallery').exists():
        page_image = PageImage.objects.filter(category='gallery').last()
    about = About.objects.last()
    gallery = Gallery.objects.all()
    # for item in gallery:
    #     print item.type_of_gallery
    context = {
        "gallery": gallery,
        "about": about,
        "page_image": page_image,
    }
    template = 'gallery-page.html'

    return render(request, template, context)


def bootick_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='bootick').exists():
        page_image = PageImage.objects.filter(category='bootick').last()
    about = About.objects.last()
    bootick = Bootick.objects.all()
    context = {"booticks": bootick, "about": about, "page_image": page_image}
    template = 'bootick.html'

    return render(request, template, context)


def license_view(request):
    about = About.objects.last()
    licenses = License.objects.all()
    context = {
        "licenses": licenses,
        "about": about,
    }
    template = 'license.html'

    return render(request, template, context)


def information_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='information').exists():
        page_image = PageImage.objects.filter(category='information').last()
    about = About.objects.last()
    context = {"about": about, "page_image": page_image}
    template = 'information.html'

    return render(request, template, context)


def public_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='publication').exists():
        page_image = PageImage.objects.filter(category='publication').last()
    about = About.objects.last()
    publics = Publication.objects.all()
    presses = Press.objects.all()
    context = {"publics": publics, "presses": presses, "about": about, "page_image": page_image}
    template = 'publick.html'

    return render(request, template, context)


def review_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='reviews').exists():
        page_image = PageImage.objects.filter(category='reviews').last()
    about = About.objects.last()
    reviews = Review.objects.filter(is_active=True)
    context = {"reviews": reviews, "about": about, "page_image": page_image}
    template = 'revius.html'

    return render(request, template, context)


def service_view(request, slug):
    about = About.objects.last()
    services = Service.objects.filter(category=slug)

    page_title = ''
    image_object = ServiceImage.objects.first()

    if slug == 'consulting':
        if ServiceImage.objects.filter(category=slug).exists():
            image_object = ServiceImage.objects.filter(category=slug).last()
        page_title = "Диагностика и консультации"

    if slug == 'medicine':
        if ServiceImage.objects.filter(category=slug).exists():
            image_object = ServiceImage.objects.filter(category=slug).last()
        page_title = "Косметология и эстетическая медицина"

    if slug == 'spa':
        if ServiceImage.objects.filter(category=slug).exists():
            image_object = ServiceImage.objects.filter(category=slug).last()
        page_title = "SPA терапия"

    if slug == 'bath_spa':
        if ServiceImage.objects.filter(category=slug).exists():
            image_object = ServiceImage.objects.filter(category=slug).last()
        page_title = "Банный SPA"

    if slug == 'art_beauty':
        if ServiceImage.objects.filter(category=slug).exists():
            image_object = ServiceImage.objects.filter(category=slug).last()
        page_title = "Арт и Бьюти студия"

    context = {
        "services": services,
        "page_title": page_title,
        "about": about,
        "service_object": image_object
    }
    template = 'service.html'

    return render(request, template, context)


def eticket_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='etiket').exists():
        page_image = PageImage.objects.filter(category='etiket').last()
    about = About.objects.last()
    context = {"about": about, "page_image": page_image}
    template = 'etiket.html'

    return render(request, template, context)


def event_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='news').exists():
        page_image = PageImage.objects.filter(category='news').last()
    about = About.objects.last()
    events = Event.objects.all()
    news = News.objects.all()
    context = {"events": events, "news": news, "about": about, "page_image": page_image}
    template = 'event.html'

    return render(request, template, context)


def certificate_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='certificates').exists():
        page_image = PageImage.objects.filter(category='certificates').last()
    about = About.objects.last()
    certificates = DiscountCertificate.objects.all()
    cards = DiscountCard.objects.all()
    context = {
        "certificates": certificates,
        "cards": cards,
        "about": about,
        "page_image": page_image
    }
    template = 'spa-sertificat.html'

    return render(request, template, context)


def partner_view(request):
    about = About.objects.last()
    partners = Partner.objects.all()
    context = {
        "partners": partners,
        "about": about
    }
    template = 'partners.html'

    return render(request, template, context)


def special_offers(request):
    page_image = PageImage.objects.first()

    offers = SpecialOffer.objects.all()

    if PageImage.objects.filter(category='special_offers').exists():
        page_image = PageImage.objects.filter(category='special_offers').last()
    about = About.objects.last()
    context = {"about": about, "page_image": page_image, "offers": offers}
    template = 'special-offers.html'

    return render(request, template, context)


def kitchen_view(request):
    page_image = PageImage.objects.first()

    if PageImage.objects.filter(category='kitchen').exists():
        page_image = PageImage.objects.filter(category='kitchen').last()
    about = About.objects.last()
    context = {"about": about, "page_image": page_image}
    template = 'spa_kitchen.html'

    return render(request, template, context)


def all_service_view(request):
    about = About.objects.last()
    context = {"about": about}
    template = 'all-service.html'

    return render(request, template, context)


def news_detail_view(request, id):
    about = About.objects.last()
    news = News.objects.get(id=id)

    context = {
        "object": news,
        "about": about
    }

    return render(request, 'news_inner.html', context)


def press_detail_view(request, id):
    about = About.objects.last()
    news = Press.objects.get(id=id)

    context = {
        "object": news,
        "about": about,
    }

    return render(request, 'press_inner.html', context)


def publick_detail_view(request, id):
    about = About.objects.last()
    news = Publication.objects.get(id=id)

    context = {
        "object": news,
        "about": about,
    }

    return render(request, 'publick_inner.html', context)


def event_detail_view(request, id):
    about = About.objects.last()
    news = Event.objects.get(id=id)

    context = {
        "object": news,
        "about": about
    }

    return render(request, 'event_inner.html', context)


def cert_detail_view(request, id):
    about = About.objects.last()
    news = DiscountCertificate.objects.get(id=id)

    context = {
        "object": news,
        "about": about
    }

    return render(request, 'cert_inner.html', context)


def card_detail_view(request, id):
    about = About.objects.last()
    news = DiscountCard.objects.get(id=id)

    context = {
        "object": news,
        "about": about
    }

    return render(request, 'card_inner.html', context)
