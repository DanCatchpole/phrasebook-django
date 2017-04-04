# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 18:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('phrasebook', '0003_auto_20170404_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
    ]