# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.sites.managers


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('fax', models.CharField(max_length=30)),
                ('website', models.URLField(max_length=300)),
                ('billing_street', models.CharField(max_length=355)),
                ('billing_state', models.CharField(max_length=255)),
                ('billing_city', models.CharField(max_length=255)),
                ('billing_zip_code', models.CharField(max_length=7)),
                ('billing_country', models.CharField(max_length=255)),
                ('shiping_street', models.CharField(max_length=355)),
                ('shiping_state', models.CharField(max_length=255)),
                ('shiping_city', models.CharField(max_length=255)),
                ('shiping_zip_code', models.CharField(max_length=7)),
                ('shiping_country', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
