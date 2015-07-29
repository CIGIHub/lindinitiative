# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_design_logo_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='footer_logo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
