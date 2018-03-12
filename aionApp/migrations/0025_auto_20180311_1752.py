# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0024_auto_20180311_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy_watche',
            name='watch',
        ),
        migrations.AddField(
            model_name='buy_watche',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='buy_watche',
            name='picture',
            field=models.ImageField(default='media/no-img.jpg', upload_to='watchPictures/'),
        ),
        migrations.AddField(
            model_name='buy_watche',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='buy_watche',
            name='user_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='buy_watche',
            name='watch_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]