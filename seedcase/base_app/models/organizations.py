"""
This file contains the base app organization model
-------------------------------------------------------------------------------
"""


from django.db import models
from .base_models import BaseModel, Address

import logging

log = logging.getLogger(__name__)


class OrganizationType(BaseModel):
    """
    This identifies an organization as University, College, Hospital
    """

    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
    )
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organization Type"
        verbose_name_plural = "Organization Types"


class Organization(BaseModel, Address):
    """
    Baseline organization info.
    """

    # Organization name
    name = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False,
    )
    note = models.TextField(max_length=500, blank=True, null=True)
    types = models.ManyToManyField(OrganizationType, blank=True)

    class Meta:
        unique_together = (
            (
                "name",
                "address",
                "address2",
                "city",
                "province",
                "country",
                "postal_code",
            ),
        )

    def __str__(self):
        return self.name
