# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class Member(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='ФИО')
    profession = models.CharField(max_length=255, verbose_name='Специализация')
    description = models.TextField(max_length=1000, verbose_name='Описание')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Спецалисты'
        verbose_name = 'Специалиста'

    def __unicode__(self):
        return smart_unicode(self.full_name)
