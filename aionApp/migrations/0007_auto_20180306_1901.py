# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0006_auto_20180306_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watche',
            name='watch_type',
            field=models.CharField(choices=[('0', 'Analog Watch'), ('1', 'Digital Watch'), ('2', 'Smart Watch')], default='0', max_length=16),
        ),
    ]
