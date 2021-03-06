# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 22:25
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_auto_20160217_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            null=True,
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
