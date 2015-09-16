# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150916_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.TextField(max_length=512, blank=True),
        ),
    ]
