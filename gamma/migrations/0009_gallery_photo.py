# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-17 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamma', '0008_auto_20170918_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
