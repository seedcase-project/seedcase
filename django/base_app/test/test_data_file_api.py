import os
from django.test import TestCase, RequestFactory
from rest_framework.parsers import FileUploadParser
from django.contrib.auth.models import Group, User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient
from base_app.models.base_models import DataFile
from base_app.views import data_files
from base_app.settings import BASE_DIR, DATA_FILE_URL


class DataFilesTestCase(TestCase):
    """
    Test the data file API endpoint
    """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.parser = FileUploadParser()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        # self.token = Token.objects.create(user=self.user)
        self.researcher_group = Group.objects.create(name='Researcher')
        self.user.groups.add(self.researcher_group)
        self.test_file_name = 'test_api_file.txt'
        self.test_file_path = os.path.join(BASE_DIR, self.test_file_name)
        try:
            # Attempt to create a new file for writing
            with open(self.test_file_path, 'x') as file:
                self.file_data = file.write('Hello, World!')
                # You can perform additional write operations if needed
        except FileExistsError:
            # File already exists, handle the case accordingly
            pass

        self.file_data = {'file': open(self.test_file_path, 'rb')}

    def test_data_files_get(self):
        request = self.factory.get(DATA_FILE_URL)
        response = data_files(request)
        self.assertEqual(response.status_code, 200)

    def test_data_files_post_authorized(self):
        self.client.force_authenticate(user=self.user)
        request = self.factory.post(DATA_FILE_URL, data=self.file_data,
                                    format='multipart')
        request.user = self.user
        response = data_files(request)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            DataFile.objects.filter(
                file__icontains=self.test_file_name).exists())

    def test_data_files_post_unauthorized(self):
        request = self.factory.post(DATA_FILE_URL, data=self.file_data,
                                    format='multipart')
        response = data_files(request)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(
            DataFile.objects.filter(
                file__icontains=self.test_file_name).exists())

    def tearDown(self):
        """
        Close the file and clean the test files
        """
        self.file_data['file'].close()
        if os.path.exists(self.test_file_path):
            # File exists, remove it
            os.remove(self.test_file_path)
