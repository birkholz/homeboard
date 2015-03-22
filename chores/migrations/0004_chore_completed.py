# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0003_auto_20150321_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='chore',
            name='completed',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
