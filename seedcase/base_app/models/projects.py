"""
This file contains the base app project model
-------------------------------------------------------------------------------
"""

from django.db import models
from .base_models import BaseModel
from .organizations import Organization
from django.contrib.auth.models import User

import logging

log = logging.getLogger(__name__)


class Project(BaseModel):
    """
    Basic project information
    """

    name = models.CharField(max_length=150, unique=True, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    stakeholder = models.ManyToManyField(
        Organization, blank=True, related_name="stake_holders"
    )
    team_member = models.ManyToManyField(User, blank=True, related_name="team_members")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
