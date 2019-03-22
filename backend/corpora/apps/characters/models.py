from django.db import models

from apps.languages.models import Language

class Character(models.Model):
    character = models.CharField(max_length=255, unique=True)
    count = models.IntegerField()
    frequency = models.FloatField(null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.character
    
    objects = models.Manager()