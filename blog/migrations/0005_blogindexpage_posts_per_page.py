# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150916_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='posts_per_page',
            field=models.IntegerField(default=10),
        ),
    ]
