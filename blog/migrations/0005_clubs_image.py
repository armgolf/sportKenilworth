# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-16 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170916_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='image',
            field=models.ImageField(default="{% static 'images/favicon (3).ico' %}", upload_to=None),
        ),
    ]
