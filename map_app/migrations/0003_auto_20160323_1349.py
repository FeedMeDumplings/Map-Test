# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0002_auto_20160323_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arealocation',
            name='rests',
        ),
        migrations.AddField(
            model_name='arealocation',
            name='rests',
            field=models.ManyToManyField(to='map_app.Rest'),
        ),
        migrations.RemoveField(
            model_name='arealocation',
            name='stations',
        ),
        migrations.AddField(
            model_name='arealocation',
            name='stations',
            field=models.ManyToManyField(to='map_app.GasStation'),
        ),
        migrations.RemoveField(
            model_name='arealocation',
            name='stores',
        ),
        migrations.AddField(
            model_name='arealocation',
            name='stores',
            field=models.ManyToManyField(to='map_app.Store'),
        ),
    ]
