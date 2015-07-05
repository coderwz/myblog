# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150626_2243'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.TextField(default=datetime.datetime(2015, 7, 5, 17, 57, 25, 846023, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
