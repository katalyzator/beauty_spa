# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-05-04 08:36
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_principe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='\u0422\u041e\u041b\u042c\u041a\u041e \u0412 \u0422\u0415\u0427\u0415\u041d\u0418\u0418 24 \u0427\u0410\u0421\u041e\u0412', verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442 \u0410\u043a\u0446\u0438\u0438')),
                ('exp_date', models.DateTimeField(help_text='\u041e\u0442\u0441\u0447\u0435\u0442 \u043d\u0430\u0447\u043d\u0435\u0442\u0441\u044f \u0441 \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u0432\u0440\u0435\u043c\u0435\u043d\u0438', verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0410\u043a\u0446\u0438\u044f',
                'verbose_name_plural': '\u0410\u043a\u0446\u0438\u044f',
            },
        ),
    ]