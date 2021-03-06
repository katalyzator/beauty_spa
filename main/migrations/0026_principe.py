# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-05-04 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20180504_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Principe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('image', models.ImageField(upload_to='images/pri_images', verbose_name='Image')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u043f\u0440\u0438\u043d\u0446\u0438\u043f',
                'verbose_name_plural': '\u041f\u0440\u0438\u043d\u0446\u0438\u043f\u044b',
            },
        ),
    ]
