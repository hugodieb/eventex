# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170809_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('talk_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Talk')),
                ('slots', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'cursos',
                'verbose_name': 'curso',
            },
            bases=('core.talk',),
        ),
    ]
