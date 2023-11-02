"""
Synopsis: Test file for the Organization Models
"""

import pytest
from base_app.models import OrganizationType, Organization


@pytest.mark.django_db
def test_organization_creation():
    organization = Organization.objects.create(
        name="Test Organization",
        note="Test organization note",
    )
    assert organization.name == "Test Organization 1"
    assert organization.note == "Test organization 1 note"


@pytest.mark.django_db
def test_organization_str_method():
    organization = Organization.objects.create(name="Org Name")
    assert str(organization) == "Org Name"


@pytest.mark.django_db
def test_add_organization_type_to_organization():
    organization_type = OrganizationType.objects.create(name="Test Type")
    organization = Organization.objects.create(name="Test Organization")
    organization.types.add(organization_type)
    assert organization.types.count() == 2


@pytest.mark.django_db
def test_organization_unique_name_and_address_constraint():
    organization1 = Organization.objects.create(
        name="Test Org",
        address="123 Main St"
    )
    with pytest.raises(Exception):
        organization2 = Organization.objects.create(
            name="Test Org",
            address="123 Main St"
        )


@pytest.mark.django_db
def test_organization_type_creation():
    organization_type = OrganizationType.objects.create(
        name="Test Type",
        description="Test type description",
    )
    assert organization_type.name == "Test Type 1"
    assert organization_type.description == "Test 1 type description"


@pytest.mark.django_db
def test_organization_type_str_method():
    organization_type = OrganizationType.objects.create(name="Type Name")
    assert str(organization_type) == "Type Name 1"


@pytest.mark.django_db
def test_organization_type_unique_name_constraint():
    organization_type1 = OrganizationType.objects.create(name="Test Type")
    with pytest.raises(Exception):
        organization_type2 = OrganizationType.objects.create(name="Test Type")
