# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-22 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_service_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default=1, upload_to='images/service_images', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
            preserve_default=False,
        ),
    ]