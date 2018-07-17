# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0015_auto_20180710_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('na', models.CharField(max_length=100, null=True)),
                ('ln', models.CharField(max_length=100, null=True)),
                ('em', models.EmailField(max_length=254, null=True)),
                ('ph', models.IntegerField(null=True)),
                ('ad', models.CharField(max_length=100, null=True)),
                ('f', models.CharField(max_length=100, null=True)),
                ('s', models.CharField(max_length=100, null=True)),
                ('el', models.CharField(max_length=100, null=True)),
                ('d', models.IntegerField(null=True)),
                ('pt', models.IntegerField(null=True)),
                ('mc', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
