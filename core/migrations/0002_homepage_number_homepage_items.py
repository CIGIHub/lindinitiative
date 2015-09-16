# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='number_homepage_items',
            field=models.IntegerField(default=3, verbose_name='Items on Homepage'),
        ),
    ]
