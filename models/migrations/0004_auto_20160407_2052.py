# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20160407_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
