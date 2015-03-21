# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20150321_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('author', models.ForeignKey(related_name='authored_bills', to=settings.AUTH_USER_MODEL)),
                ('home', models.ForeignKey(related_name='bills', to='home.Home')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
