# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0037_auto_20170219_1658'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Schedule497Filing',
            new_name='Form497Filing',
        ),
        migrations.RenameModel(
            old_name='Schedule497FilingVersion',
            new_name='Form497FilingVersion',
        ),
        migrations.RenameModel(
            old_name='Schedule497Part1Item',
            new_name='Form497Part1Item',
        ),
        migrations.RenameModel(
            old_name='Schedule497Part1ItemVersion',
            new_name='Form497Part1ItemVersion',
        ),
        migrations.RenameModel(
            old_name='Schedule497Part2Item',
            new_name='Form497Part2Item',
        ),
        migrations.RenameModel(
            old_name='Schedule497Part2ItemVersion',
            new_name='Form497Part2ItemVersion',
        ),
    ]
