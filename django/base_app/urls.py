"""base_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import home_page, organization_list, project_list, all_organizations
from .views import raw_file_upload
from project_app.urls import urlpatterns as project_app_urls
from django.conf import settings

# Setup default API View
schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="API documentation for Seedcase",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myproject.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('organizations/', organization_list, name='organizations'),
    path('projects/', project_list, name='projects'),
    path('api/organizations/', all_organizations, name='api_organizations'),
    path('datafile/', raw_file_upload, name='raw_file_upload'),
    re_path(r'^datafile/(?P<path>.*)$', serve, {'document_root':
                                          settings.DATA_FILE_ROOT}),
]

# Add other apps url to the base app
urlpatterns += project_app_urls

admin.site.index_title = "Seedcase Portal Administration"
admin.site.site_header = "Seedcase Portal Administration"
admin.site.site_title = "Seedcase Portal Administration"
