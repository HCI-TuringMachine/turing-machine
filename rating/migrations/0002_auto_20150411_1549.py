# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestor',
            name='joined_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='worker',
            name='joined_date',
            field=models.DateTimeField(default=None),
        ),
    ]
