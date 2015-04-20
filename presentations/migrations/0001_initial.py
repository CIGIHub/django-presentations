# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedSlides',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('title', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('title', models.CharField(max_length=1024)),
                ('body', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='presentation',
            name='slides',
            field=models.ManyToManyField(to='presentations.Slide', blank=True, null=True, through='presentations.OrderedSlides'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderedslides',
            name='presentation',
            field=models.ForeignKey(to='presentations.Presentation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderedslides',
            name='slide',
            field=models.ForeignKey(to='presentations.Slide'),
            preserve_default=True,
        ),
    ]
