"""
Copyright 2022 AARHUS UNIVERSITY All rights reserved
Developed by Richard Ding
-------------------------------------------------------------------------------
"""

from django.contrib import admin
from .models import Organization, OrganizationType, Project


@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'organizations', ]
    search_fields = ['name', ]

    def organizations(self, org_type):

        return ', '.join(list(Organization.objects.filter(types=org_type).values_list(
            'name', flat=True
        )))


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'organization_types', 'city', 'province', 'country',
    ]
    search_fields = ('id', 'name',)
    ordering = ('name', 'id',)
    list_filter = ('types',)

    def organization_types(self, org):
        return ', '.join(list(org.types.values_list('name', flat=True)))


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stake_holders', 'team_members')
    search_fields = ('id', 'name',)
    ordering = ('name', 'id',)
    list_filter = ('name',)

    def stake_holders(self, proj):
        return ', '.join(list(proj.stakeholder.values_list('name', flat=True)))

    def team_members(self, proj):
        return ', '.join(list(proj.team_member.values_list('username', flat=True)))


