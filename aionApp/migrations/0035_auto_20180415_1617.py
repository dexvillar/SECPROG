# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-15 16:17
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0034_watche_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_addres',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='shipping_addres',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
