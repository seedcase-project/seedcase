"""
This file contains the project data app django model
-------------------------------------------------------------------------------
"""

from django.db import models
from base_app.models import Project

class ObservationalUnit(models.Model):
    """
    Model to store information about the observational unit for a project.
    """
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    observational_unit_id = models.CharField(max_length=100, unique=True)
    collection_datetime = models.DateTimeField()

    def __str__(self):
        return self.observational_unit_id
