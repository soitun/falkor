# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falkor', '0005_auto_20161102_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='editortype',
            name='urlPrefix',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='editortype',
            name='urlSuffix',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
