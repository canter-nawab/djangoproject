# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-17 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181117_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_id', models.IntegerField(default=0)),
                ('installment_price', models.IntegerField(blank=True, null=True)),
                ('receiving_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('total_price', models.PositiveIntegerField(blank=True, null=True)),
                ('no_of_installments', models.PositiveIntegerField(blank=True, null=True)),
                ('installation_date', models.DateTimeField(blank=True, null=True)),
                ('removal_date', models.DateTimeField(blank=True, null=True)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Banners')),
            ],
            options={
                'verbose_name_plural': 'User',
            },
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
