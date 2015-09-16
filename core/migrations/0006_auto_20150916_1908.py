# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_lindbasepage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lindbasepage',
            name='short_description',
            field=models.CharField(max_length=256),
        ),
    ]
