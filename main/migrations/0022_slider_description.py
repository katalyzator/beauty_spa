# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20180430_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
    ]
