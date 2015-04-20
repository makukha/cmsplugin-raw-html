# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_migrate_use_structure'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawHtmlPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True, serialize=False)),
                ('body', models.TextField(verbose_name='HTML')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
