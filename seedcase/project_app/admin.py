"""
This file contains the project data app django admin configurations
-------------------------------------------------------------------------------
"""

from django.contrib import admin
from base_app.models import Project
from .models import ObservationalUnit


class ObservationalUnitAdmin(admin.ModelAdmin):
    """
    List all the information in the table on the observational unit.
    """

    list_display = (
        "observational_unit_id",
        "collection_datetime",
        "project"
    )
    list_filter = ("project")

    def get_queryset(self, request):
        """
        get_queryset Function to limit the query of the table to only those with
        admin permissions.

        Parameters
        ----------
        request : _type_
            Which data to show when querying the table.

        Returns
        -------
        _type_
            _description_
        """
        
        # Retrieve the IDs of projects where the user is a team member
        team_member_projects = Project.objects.filter(
            team_member=request.user
        ).values_list("id", flat=True)

        # Filter the participants based on the user's project IDs
        queryset = (
            super().get_queryset(request).filter(project__in=team_member_projects)
        )
        return queryset


admin.site.register(ObservationalUnit, ObservationalUnitAdmin)
