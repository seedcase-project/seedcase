"""
Synopsis: Test file for the Project Model
"""

import pytest
from base_app.models import Project, Organization
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_project_creation():
    project = Project.objects.create(
        name="Test Project",
        description="Test project description",
    )
    assert project.name == "Test Project"
    assert project.description == "Test project description"


@pytest.mark.django_db
def test_project_str_method():
    project = Project.objects.create(name="Project Name")
    assert str(project) == "Project Name"


@pytest.mark.django_db
def test_add_stakeholder_to_project():
    project = Project.objects.create(name="Test Project")
    organization = Organization.objects.create(name="Test Org")
    project.stakeholder.add(organization)
    assert project.stakeholder.count() == 1


@pytest.mark.django_db
def test_add_team_member_to_project():
    project = Project.objects.create(name="Test Project")
    user = User.objects.create(username="test_user")
    project.team_member.add(user)
    assert project.team_member.count() == 1


@pytest.mark.django_db
def test_project_unique_name_constraint():
    project1 = Project.objects.create(name="Test Project")
    with pytest.raises(Exception):
        project2 = Project.objects.create(name="Test Project")


@pytest.mark.django_db
def test_project_unique_name_max_length():
    long_name = "a" * 151  # Exceeds the max length
    with pytest.raises(Exception):
        project = Project.objects.create(name=long_name)



