# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrasebook', '0005_language_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='shortened',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
    ]
