# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(help_text='\u0420\u0430\u0437\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c 390x300', upload_to='images/specialists', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
    ]
