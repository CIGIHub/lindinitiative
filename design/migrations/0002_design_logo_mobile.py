# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='logo_mobile',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
