from django import forms
from django.db import models

from scrum.models import Project

class ProjectAssignmentForm(models.Model):
    project = forms.ModelChoiceField(queryset = Project.objects.all())
