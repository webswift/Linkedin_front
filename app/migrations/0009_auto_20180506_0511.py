# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-05 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='enable_proxy',
            field=models.BooleanField(default=True),
        ),
    ]
