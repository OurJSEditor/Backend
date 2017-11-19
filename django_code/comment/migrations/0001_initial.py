# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-24 16:01
from __future__ import unicode_literals

import comment.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('program', '0002_program_created'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.CharField(default=comment.models.generate_comment_id, max_length=10, primary_key=True, serialize=False)),
                ('depth', models.IntegerField()),
                ('reply_count', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField(blank=True)),
                ('original_content', models.TextField(blank=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.Comment')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]