# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='count',
            name='user',
        ),
        migrations.DeleteModel(
            name='Count',
        ),
    ]
