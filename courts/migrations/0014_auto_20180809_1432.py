# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-09 14:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0013_auto_20180809_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='court',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
