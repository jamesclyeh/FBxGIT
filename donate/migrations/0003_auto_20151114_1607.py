# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_auto_20151114_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ID',
            new_name='FB_ID',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='created_at',
            new_name='joined',
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.CharField(default=b'C', max_length=100, choices=[(b'C', b'Clothes'), (b'M', b'Makeup and Cosmetics'), (b'O', b'Others')]),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=254, verbose_name=b'email address', db_index=True),
        ),
    ]
