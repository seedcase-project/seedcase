"""
This file contains the project data app django model
-------------------------------------------------------------------------------
"""


from django.db import models
from django.db.models import JSONField
from base_app.models import Project


class Project_data(models.Model):
    """
    Raw project data presentation, could be manually input.
    """
    label = models.CharField(max_length=100, unique=True, null=False, blank=False,)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    raw_data = JSONField(blank=True, null=True)

    def __str__(self):
        return self.label

