"""
This file contains the project data app django model
-------------------------------------------------------------------------------
"""

from django.db import models
from base_app.models import Project


class Participant(models.Model):
    """
    Model to store participant information for a project.
    """

    # TODO add more choices
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    MARITAL_STATUS_CHOICES = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('O', 'Other'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    participant_id = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    race = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    # TODO could make the language as language choices
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.participant_id