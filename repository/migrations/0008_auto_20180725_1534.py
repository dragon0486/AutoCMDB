# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-25 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_networkdevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetrecord',
            name='asset_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar', to='repository.Asset'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disk', to='repository.Server'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory', to='repository.Server'),
        ),
        migrations.AlterField(
            model_name='nic',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nic', to='repository.Server'),
        ),
    ]
