# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-28 16:36
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ponto1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('ponto1', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('ponto2', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
