# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20171001_2333'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserList',
        ),
    ]