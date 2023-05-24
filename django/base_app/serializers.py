from rest_framework import serializers
from .models import UploadedFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'

    def create(self, validated_data):
        file = validated_data['file']  # Assuming the field name for the file is 'file'
        uploaded_file = UploadedFile.objects.create(file=file)
        return uploaded_file