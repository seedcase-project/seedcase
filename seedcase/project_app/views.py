"""
This file contains the project data app API functions
-------------------------------------------------------------------------------
"""

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Project_data


def _serialize_project_data(project_data):
    return {
        'id': project_data.id,
        'project_name': project_data.project.name,
        'description': project_data.description,
        'project_data': project_data.raw_data,
    }


@api_view(['GET'])
def project_data(request, project_data_id=None):
    """
    Project data API endpoint
    Retrieve all project data if project_name is not provide
    """
    if project_data_id is None:
        project_data_all = Project_data.objects.all()
        project_data_objects = [_serialize_project_data(data) for data in project_data_all]

    else:
        data_obj = Project_data.objects.get(pk=project_data_id)
        project_data_objects = _serialize_project_data(data_obj)

    return Response(data=project_data_objects, status=status.HTTP_200_OK)


def project_data_list(request):
    context = {}
    project_data_all = Project_data.objects.all()
    context['project_data_list'] = project_data_all
    return render(request, 'project_data.html', context)
