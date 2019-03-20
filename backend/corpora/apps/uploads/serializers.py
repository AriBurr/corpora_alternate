from rest_framework import serializers
from django.contrib.auth.models import User

from .models import FileUpload, URLUpload

class URLUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLUpload
        fields = ('title', 'url', 'language_id')
        # fields = '__all__'

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('title', 'file', 'file_type', 'language_id')
        # fields = '__all__'
    