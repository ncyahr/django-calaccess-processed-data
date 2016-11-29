# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0003_auto_20161129_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='form460schedulehitem',
            name='reported_on_h1',
            field=models.BooleanField(default=False, help_text='Indicates if the item was actually reported on Part 1 of Schedule H. Until 2001, campaign filers were required to report loans made to others on Part 1 of Schedule H, separate from repayments or forgiveness of those loans (Schedule H, Part 2)', verbose_name='reported on H1'),
        ),
        migrations.AddField(
            model_name='form460schedulehitemversion',
            name='reported_on_h1',
            field=models.BooleanField(default=False, help_text='Indicates if the item was actually reported on Part 1 of Schedule H. Until 2001, campaign filers were required to report loans made to others on Part 1 of Schedule H, separate from repayments or forgiveness of those loans (Schedule H, Part 2)', verbose_name='reported on H1'),
        ),
    ]
