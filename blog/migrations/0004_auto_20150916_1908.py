# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='short_description',
            field=models.CharField(max_length=256),
        ),
    ]
