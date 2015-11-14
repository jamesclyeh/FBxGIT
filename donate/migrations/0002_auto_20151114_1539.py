# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('ID', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='picture',
            field=models.ImageField(default='test', upload_to=b'pictures/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='status',
            field=models.CharField(default=b'U', max_length=100, choices=[(b'U', b'UNSOLD'), (b'S', b'SOLD')]),
        ),
        migrations.AddField(
            model_name='goods',
            name='comsumer',
            field=models.ForeignKey(related_name='goods_consumer', to='donate.User', null=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='donor',
            field=models.ForeignKey(related_name='goods_donor', default='test', to='donate.User'),
            preserve_default=False,
        ),
    ]
