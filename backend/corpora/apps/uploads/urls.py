from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.UploadView.as_view(), name='upload_view'),
    path('upload_file/', views.UploadFileView.as_view(), name="upload_file"),
    path('upload_url/', views.UploadURLView.as_view(), name="upload_url"),
]
