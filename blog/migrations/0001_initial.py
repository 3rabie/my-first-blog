# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Title', models.CharField(max_length=200)),
                ('Text', models.TextField()),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Published_date', models.DateTimeField(null=True, blank=True)),
                ('Auther', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
