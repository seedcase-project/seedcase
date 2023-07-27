"""
Project Data URL path configuration
"""

from django.urls import path
from .views import project_data, project_data_list

urlpatterns = [
    path('project_app/', project_data_list, name='project_data'),
    path('project_app/api/data_list/', project_data, name='all_project_data'),
    path('project_app/api/data_list/<int:project_data_id>/', project_data, name='project_data_list'),
]