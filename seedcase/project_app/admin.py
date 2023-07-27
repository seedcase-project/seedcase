"""
This file contains the project data app django admin configurations
-------------------------------------------------------------------------------
"""

from django.contrib import admin
from .models import Project_data


@admin.register(Project_data)
class ProjectDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'label', 'description')
    search_fields = ('project__name', 'label', 'description')
    ordering = ('id',)

    def project_name(self, obj):
        return obj.project.name