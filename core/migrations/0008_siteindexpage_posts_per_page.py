# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_siteindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteindexpage',
            name='posts_per_page',
            field=models.IntegerField(default=10),
        ),
    ]
