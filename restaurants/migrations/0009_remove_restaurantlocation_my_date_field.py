# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-07 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_restaurantlocation_my_date_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='my_date_field',
        ),
    ]