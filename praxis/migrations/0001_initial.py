# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-03 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titel')),
                ('content', models.TextField(help_text='HTML-Tags sind erlaubt.', verbose_name='Inhalt')),
                ('weight', models.IntegerField(default=0, help_text='Je größer die Zahl, desto weiter unten/hinten erscheint der Abschnitt.', verbose_name='Gewichtung')),
            ],
            options={
                'verbose_name_plural': 'Abschnitte',
                'verbose_name': 'Abschnitt',
            },
        ),
    ]
