# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-23 18:22
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('courts', '0004_court_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
