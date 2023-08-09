from rest_framework import serializers
from .models import DataFile


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataFile
        fields = "__all__"

    def create(self, validated_data):
        file = validated_data["file"]
        uploaded_file = DataFile.objects.create(file=file)
        return uploaded_file
