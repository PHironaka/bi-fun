# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-01 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20180601_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]