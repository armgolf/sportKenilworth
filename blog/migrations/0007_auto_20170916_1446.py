# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-16 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_clubs_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='image',
            field=models.CharField(default='imagelinkhere', max_length=500),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='cost',
            field=models.CharField(max_length=100),
        ),
    ]
