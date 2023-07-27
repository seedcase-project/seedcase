"""
Synopsis: Test file for the Organization Models
"""

import pytest
from base_app.models.organizations import *

@pytest.mark.django_db
def test_organization_creation():
    """
    Test that the organization is created correctly.
    """
    org_type = OrganizationType.objects.create(name='University', description='University organization')
    org = Organization.objects.create(name='Test Organization', note='This is a test organization')
    org.types.add(org_type)
    assert org.name == 'Test Organization'
    assert org.note == 'This is a test organization'
    assert org.types.count() == 1

@pytest.mark.django_db
def test_organization_type_creation():
    """
    Test that organization type is created correctly.
    """
    org_type = OrganizationType.objects.create(name='University', description='University organization')
    assert org_type.name == 'University'
    assert org_type.description == 'University organization'







