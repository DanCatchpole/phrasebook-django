# Generated by Django 2.1 on 2018-08-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrasebook', '0014_category_share_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='share_url',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
