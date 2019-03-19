from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status

from .models import FileUpload, URLUpload
from .serializers import FileUploadSerializer, URLUploadSerializer
from .services import URLUploadService

class UploadView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'upload_form/form.html'
    def get(self, request):
        queryset = FileUpload.objects.all()
        return Response({'uploads': queryset})

class SuccessView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'upload_form/success.html'

class FailureView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'upload_form/failure.html'

class UploadFileView(APIView):
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # parsed = URLUpload.url_check(request.data['url'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UploadURLView(APIView):
    def post(self, request):
        serializer = URLUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # parsed = URLUpload.url_check(request.data['url'])
            parsed = URLUploadService.parse_url(request.data['url'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
