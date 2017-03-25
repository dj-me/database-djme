# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='djsessions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member', models.CharField(default=b'NULL', max_length=250)),
                ('hostname', models.ForeignKey(to='main.user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='finalplaylist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostedsession', models.CharField(default=b'NULL', max_length=250)),
                ('counter', models.CharField(default=b'NULL', max_length=250)),
                ('hostname', models.ForeignKey(to='main.user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
