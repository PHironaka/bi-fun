# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-02 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_auto_20180202_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='court',
            options={},
        ),
        migrations.RemoveField(
            model_name='court',
            name='timestamp',
        ),
    ]