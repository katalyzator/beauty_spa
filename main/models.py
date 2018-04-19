# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class Member(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='ФИО')
    profession = models.CharField(max_length=255, verbose_name='Специализация')
    description = models.TextField(max_length=1000, verbose_name='Описание')

    image = models.ImageField(upload_to='images/specialists', verbose_name='Картинка',
                              help_text='Размер картинки должен быть 390x300')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Спецалисты'
        verbose_name = 'Специалиста'

    def __unicode__(self):
        return smart_unicode(self.full_name)


class Review(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    text = models.TextField(verbose_name='Текст')
    is_active = models.BooleanField(default=False, verbose_name='Активность',
                                    help_text='Поставьте галочку, чтобы вывести на сайте')
    image = models.ImageField(upload_to='images/reviews_images', verbose_name='Картинка')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

    def __unicode__(self):
        return smart_unicode(self.full_name)


class Service(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    duration = models.IntegerField(default=1, verbose_name='Длительность в днях')
    price = models.CharField(max_length=300, verbose_name='Ценообразование',
                             help_text='Пример: (от 1200 - 3000 за 1приход)')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'Услугу'

    def __unicode__(self):
        return smart_unicode(self.title)


class DiscountCertificate(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    tag = models.CharField(max_length=255, verbose_name='Тэг', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=255, verbose_name='Цена')
    is_active = models.BooleanField(default=False, verbose_name='Активность',
                                    help_text='Поставьте галочку, чтобы вывести на сайте')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Подарочные сертификаты'
        verbose_name = 'Сертификат'

    def __unicode__(self):
        return smart_unicode(self.title)


class DiscountCard(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    tag = models.CharField(max_length=255, verbose_name='Тэг', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=255, verbose_name='Цена')
    is_active = models.BooleanField(default=False, verbose_name='Активность',
                                    help_text='Поставьте галочку, чтобы вывести на сайте')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Подарочные Карты'
        verbose_name = 'Карту'

    def __unicode__(self):
        return smart_unicode(self.title)


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    logo = models.ImageField(upload_to='images/partners_images', verbose_name='Логотип объекта')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Партнеры'
        verbose_name = 'Партнера'

    def __unicode__(self):
        return smart_unicode(self.name)


class Gallery(models.Model):
    GALLERY_TYPE = (
        ('interior', 'Интерьер'),
        ('world_of_beauty', 'Мир Beauty Spa'),
        ('products', 'Продукция'),
        ('life_style', 'Стиль жизни'),
    )
    title = models.CharField(max_length=255, verbose_name='Название картинки')
    image = models.ImageField(upload_to='images/gallery_images', verbose_name='Картинка')
    type_of_gallery = models.CharField(choices=GALLERY_TYPE, max_length=255, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Галерея'
        verbose_name = 'Картинку'

    def __unicode__(self):
        return smart_unicode(self.title)


class License(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название лицензии')
    image = models.ImageField(upload_to='images/license_images', verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Лицензии'
        verbose_name = 'Картинку'

    def __unicode__(self):
        return smart_unicode(self.title)


class Slider(models.Model):
    title = models.CharField(max_length=800, verbose_name='Заголовок')
    image = models.ImageField(upload_to='images/slider_images', verbose_name='Картинка')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Слайдеры'
        verbose_name = 'Слайд'

    def __unicode__(self):
        return smart_unicode(self.title)
