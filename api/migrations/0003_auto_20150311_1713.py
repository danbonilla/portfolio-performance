# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150311_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benchmarkhistory',
            old_name='month',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='portfoliohistory',
            old_name='month',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='benchmarkhistory',
            name='growth',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='portfoliohistory',
            name='growth',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
