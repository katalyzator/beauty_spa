# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_promotion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='duration',
        ),
    ]
