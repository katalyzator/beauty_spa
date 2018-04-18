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
