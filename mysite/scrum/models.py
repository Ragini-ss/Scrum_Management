from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms
from django.forms import PasswordInput

# Create your models here.
    
class Project(models.Model):
    STATUS_CHOICE = (
        ('start', 'Start'),
        ('completed', 'Completed'),
        ('dormant', 'Dormant'),
        ('active', 'Active'),
    )
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    slug = models.SlugField(max_length = 100, unique = True)
    start = models.DateTimeField(default=timezone.now)
    finish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='start')
    owner = models.ForeignKey(User, related_name = 'projects_created')
    target_estimate = models.IntegerField()
    members = models.ManyToManyField(User, verbose_name="Projects Assigned", related_name = 'projects_assigned', blank = True)

    def project_members(self):
        return ', '.join([obj.username for obj in self.members.all()])
    project_members.short_description = 'Members'
    project_members.allow_tags = True
    
    class Meta:
      db_table = "Project"
      ordering = ('start',)

    def __str__(self):
      return self.title

class Sprint(models.Model):
    STATUS_CHOICE = (
        ('started', 'Started'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 100, unique = True)
    days = models.IntegerField(default=14)
    project_title = models.ForeignKey(Project, related_name = 'include_sprints')
    dateadded = models.DateTimeField(default=timezone.now)
    gap = models.IntegerField(default=0)
    # backlog_status = models.CharField(max_length=10,
    #                          choices=STATUS_CHOICE,
    #                          default='start')
    
    class Meta:
      db_table = "Sprint"
      ordering = ('project_title',)

    def __str__(self):
      return self.title
    
class Backlog(models.Model):
    TYPE_CHOICE = (
        ('feature', 'Feature'),
        ('defect', 'Defect'),
    )
    PRIORITY_CHOICE = (
        ('blocker', 'Blocker'),
        ('critical', 'Critical'),
        ('major', 'Major'),
        ('minor', 'Minor'),
        ('trivial', 'Trivial')
    )
    STATUS_CHOICE = (
        ('open', 'Open'),
        ('in progress', 'In progress'),
        ('completed', 'Completed'),
    )
    
    project_name = models.ForeignKey(Project, related_name = 'project_name')
    btype = models.CharField(max_length=10,
                              choices=TYPE_CHOICE,
                              default='feature')
    slug = models.SlugField(max_length = 100, unique = True)
    title = models.CharField(max_length = 250)
    dateadded = models.DateTimeField(default=timezone.now)
    priority = models.CharField(max_length=10,
                              choices=PRIORITY_CHOICE,
                              default='major')
    duedate = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='start')
    sprint_name = models.ForeignKey(Sprint, related_name = 'backlogs', verbose_name='Sprint')
    description = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
      db_table = "Backlog"
      ordering = ('project_name',)

    def __str__(self):
      return self.title

'''class AssignMemberToProject(models.Model):
    STATUS_CHOICE = (
        ('start', 'Start'),
        ('completed', 'Completed'),
        ('dormant', 'Dormant'),
        ('active', 'Active'),
    )
    title = models.CharField(max_length=250)
    dateadded = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='start')
    class Meta:
      db_table = "Assign Members to Project"
      ordering = ('dateadded',)

    def __str__(self):
      return self.title

   
class BeginProject(models.Model):
    STATUS_CHOICE = (
        ('start', 'Start'),
        ('completed', 'Completed'),
        ('dormant', 'Dormant'),
        ('active', 'Active'),
    )
    title = models.CharField(max_length=250)
    dateadded = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='start')
    class Meta:
      db_table = "Begin Project"
      ordering = ('title',)

    def __str__(self):
      return self.title'''
    
