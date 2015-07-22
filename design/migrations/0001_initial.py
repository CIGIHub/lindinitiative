# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('default', models.BooleanField(default=False)),
                ('logo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('background_image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
        ),
    ]
