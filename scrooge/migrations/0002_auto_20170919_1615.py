# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrooge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costbreakdown',
            name='user_groups',
            field=models.ManyToManyField(blank=True, default=None, to='scrooge.UserGroup'),
        ),
    ]
