# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20170925_1339'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]