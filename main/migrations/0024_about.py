# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-05-04 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20180502_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 1')),
                ('phone_number_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 2')),
                ('description', models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u043e\u0431\u044a\u0435\u043a\u0442',
                'verbose_name_plural': '\u041e \u041d\u0430\u0441',
            },
        ),
    ]