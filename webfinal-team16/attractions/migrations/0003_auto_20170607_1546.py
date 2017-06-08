# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0002_auto_20170606_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='food1_content',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='food1_place',
            field=models.CharField(default='Taipei', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='food2_content',
            field=models.CharField(default='Taipei', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='food2_place',
            field=models.CharField(default='Taipeo', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='food3_content',
            field=models.CharField(default='good', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='food3_place',
            field=models.CharField(default='Taipei', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='photo_food1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_food2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_food3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]