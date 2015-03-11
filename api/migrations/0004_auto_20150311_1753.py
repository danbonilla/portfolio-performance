# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150311_1713'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Portfolio',
            new_name='Portfolios',
        ),
    ]
