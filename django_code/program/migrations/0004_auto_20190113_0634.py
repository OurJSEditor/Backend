# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-13 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_vote_counts'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='last_published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='published_messsage',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
