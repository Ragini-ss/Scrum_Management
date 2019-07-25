# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0002_project_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlog',
            name='sprint_name',
            field=models.ForeignKey(related_name='backlogs', default=0, verbose_name='Sprint', blank=True, to='scrum.Sprint'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projects_assigned', verbose_name='Projects Assigned', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
