from django.db import models
from django.contrib.auth.models import User

from apps.languages.models import Language

class FileUpload(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/')
    file_type = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title

    objects = models.Manager()

class URLUpload(models.Model):
    title = models.TextField()
    url = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    objects = models.Manager()
