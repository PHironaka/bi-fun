# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-03 05:20
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0007_auto_20180630_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
