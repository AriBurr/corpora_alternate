from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadView.as_view(), name='upload_view'),
    path('success/', views.SuccessView.as_view(), name="success"),
    path('failure/', views.FailureView.as_view(), name="failure"),
    path('upload_file/', views.UploadFileView.as_view(), name="upload_file"),
    path('upload_url/', views.UploadURLView.as_view(), name="upload_url")
]