# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150321_1442'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='User',
        ),
    ]
