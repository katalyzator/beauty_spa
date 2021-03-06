# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 11:45
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_pageimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('card_club', '\u041a\u043b\u0443\u0431\u043d\u044b\u0435 \u043a\u0430\u0440\u0442\u044b Beauty SPA'), ('promotion', '\u0411\u043e\u043d\u0443\u0441\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430'), ('spa_party', 'Spa \u0432\u0435\u0447\u0435\u0440\u0438\u043d\u043a\u0438'), ('season_offer', '\u0421\u0435\u0437\u043e\u043d\u043d\u044b\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f')], max_length=150, verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f',
            },
        ),
    ]
