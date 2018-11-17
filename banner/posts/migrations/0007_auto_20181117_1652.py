# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-17 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20181117_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banners',
            old_name='thread',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]