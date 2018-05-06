# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-05-04 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
    ]