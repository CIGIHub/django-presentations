# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0002_auto_20150420_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='slides',
            field=models.ManyToManyField(to='presentations.Slide', through='presentations.OrderedSlides'),
        ),
    ]
