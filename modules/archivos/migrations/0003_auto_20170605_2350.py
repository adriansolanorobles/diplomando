# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-05 23:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0002_archivo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archivo',
            old_name='etata',
            new_name='etapa',
        ),
    ]
