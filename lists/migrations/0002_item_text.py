# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-16 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
