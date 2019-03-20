from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status

from .models import FileUpload, URLUpload
from .serializers import FileUploadSerializer, URLUploadSerializer
from .services import FileUploadService, URLUploadService

class UploadView(ListAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    def get(self, request):
        queryset = self.get_queryset()
        serializer = FileUploadSerializer(queryset, many=True)
        return Response(serializer.data)

class UploadFileView(APIView):
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            FileUploadService.parse_file_type()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UploadURLView(APIView):
    def post(self, request):
        serializer = URLUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            URLUploadService.parse_url(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)