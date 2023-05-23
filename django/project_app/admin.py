"""
This file contains the project data app django admin configurations
-------------------------------------------------------------------------------
"""

from django.contrib import admin
from base_app.models import Project
from .models import Participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
    'participant_id', 'project', 'gender', 'date_of_birth', 'race',
    'marital_status', 'language')
    list_filter = ('project',)

    def get_queryset(self, request):
        # Retrieve the IDs of projects where the user is a team member
        team_member_projects = Project.objects.filter(
            team_member=request.user).values_list('id', flat=True)

        # Filter the participants based on the user's project IDs
        queryset = super().get_queryset(request).filter(
            project__in=team_member_projects)
        return queryset


admin.site.register(Participant, ParticipantAdmin)
