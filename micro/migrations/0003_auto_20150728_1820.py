# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0002_auto_20150728_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microsection',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='microsection',
            name='heading',
            field=models.CharField(max_length=512),
        ),
    ]
