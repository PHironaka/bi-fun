# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-30 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0006_courtimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courtimage',
            name='post',
        ),
        migrations.DeleteModel(
            name='CourtImage',
        ),
    ]