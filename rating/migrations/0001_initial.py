# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requestor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reqid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('pay', models.PositiveSmallIntegerField()),
                ('fair', models.PositiveSmallIntegerField()),
                ('fast', models.PositiveSmallIntegerField()),
                ('comm', models.PositiveSmallIntegerField()),
                ('num_of_reports', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestorRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.PositiveSmallIntegerField()),
                ('requestor', models.ForeignKey(to='rating.Requestor')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workerid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.PositiveSmallIntegerField()),
                ('requestor', models.ForeignKey(to='rating.Requestor')),
                ('worker', models.ForeignKey(to='rating.Worker')),
            ],
        ),
        migrations.AddField(
            model_name='requestorrating',
            name='worker',
            field=models.ForeignKey(to='rating.Worker'),
        ),
    ]
