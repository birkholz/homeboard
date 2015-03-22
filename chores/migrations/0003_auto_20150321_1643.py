# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0002_auto_20150321_0006'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together=set([('user', 'chore')]),
        ),
    ]
