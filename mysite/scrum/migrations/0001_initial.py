# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btype', models.CharField(default='feature', max_length=10, choices=[('feature', 'Feature'), ('defect', 'Defect')])),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('title', models.CharField(max_length=250)),
                ('dateadded', models.DateTimeField(default=django.utils.timezone.now)),
                ('priority', models.CharField(default='major', max_length=10, choices=[('blocker', 'Blocker'), ('critical', 'Critical'), ('major', 'Major'), ('minor', 'Minor'), ('trivial', 'Trivial')])),
                ('duedate', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='start', max_length=10, choices=[('open', 'Open'), ('in progress', 'In progress'), ('completed', 'Completed')])),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
                'ordering': ('project_name',),
                'db_table': 'Backlog',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('finish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='start', max_length=10, choices=[('start', 'Start'), ('completed', 'Completed'), ('dormant', 'Dormant'), ('active', 'Active')])),
                ('target_estimate', models.IntegerField()),
                ('owner', models.ForeignKey(related_name='projects_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('start',),
                'db_table': 'Project',
            },
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('days', models.IntegerField(default=14)),
                ('dateadded', models.DateTimeField(default=django.utils.timezone.now)),
                ('gap', models.IntegerField(default=0)),
                ('project_title', models.ForeignKey(related_name='include_sprints', to='scrum.Project')),
            ],
            options={
                'ordering': ('project_title',),
                'db_table': 'Sprint',
            },
        ),
        migrations.AddField(
            model_name='backlog',
            name='project_name',
            field=models.ForeignKey(related_name='project_name', to='scrum.Project'),
        ),
    ]
