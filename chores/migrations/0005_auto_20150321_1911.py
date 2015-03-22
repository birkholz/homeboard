# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0004_chore_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
