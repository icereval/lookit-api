# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-17 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20170814_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='contact_name',
            new_name='nickname',
        ),
    ]