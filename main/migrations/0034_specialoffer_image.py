# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_specialoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='image',
            field=models.ImageField(default=1, upload_to='images/special_offers'),
            preserve_default=False,
        ),
    ]
