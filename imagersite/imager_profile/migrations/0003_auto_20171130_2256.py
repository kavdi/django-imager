# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-30 22:56
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0002_auto_20171130_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]
