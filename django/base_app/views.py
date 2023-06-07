"""
This file contains the base app API functions
-------------------------------------------------------------------------------
"""

from django.shortcuts import render
from .models.organizations import Organization, OrganizationType
from .models.projects import Project
from .models import DataFile
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .serializers import FileSerializer


def _serialize_organization_type(org_type):
    return {
        'id': org_type.id,
        'name': org_type.name,
    }


def _serialize_organization(org):
    return {
        'id': org.id,
        'name': org.name,
        'types': [_serialize_organization_type(t) for t in org.types.all()],
    }


@api_view(['GET'])
def all_organizations(request, type=None):
    """
    List all Organizations.
    If 'type' specified (either by ID or by name), filter to that type.
    """
    orgs = Organization.objects.all().prefetch_related('types').order_by('name')
    if type is not None:
        try:
            # This line will throw a ValueError if it's not an integer,
            # which means it should be a string representing the type name.
            type_id = int(type)
            try:
                org_type = OrganizationType.objects.get(pk=type_id)
            except OrganizationType.DoesNotExist:
                return Response(_('OrganizationType {} not found').format(type),
                                status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            try:
                org_type = OrganizationType.objects.get(name=str(type))
            except (OrganizationType.DoesNotExist,
                    OrganizationType.MultipleObjectsReturned):
                return Response(_('OrganizationType {} not found').format(type),
                                status=status.HTTP_404_NOT_FOUND)
        orgs = orgs.filter(types=org_type)
    org_objects = [_serialize_organization(org) for org in orgs]
    return Response(org_objects)


def home_page(request):
    return render(request, 'index.html')


def organization_list(request):
    context = {}
    organization_all = Organization.objects.all()
    context['organization_list'] = organization_all
    return render(request, 'organizations.html', context)


def project_list(request):
    context = {}
    project_all = Project.objects.all()
    context['project_list'] = project_all
    return render(request, 'projects.html', context)


@api_view(['POST', 'GET'])
def data_files(request, format=None):
    """
    Call this function List all uploaded data files.
    Post to upload the file to the endpoint.
    """
    parser_classes = [FileUploadParser]  # Specify the file upload parser

    if request.method == 'GET':
        files = DataFile.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user.groups.filter(name='Researcher').exists():
            file_serializer = FileSerializer(data=request.data)

            if file_serializer.is_valid():
                file_serializer.save()
                return Response(file_serializer.data,
                                status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("You are not authorized to use this API",
                            status=status.HTTP_401_UNAUTHORIZED)
