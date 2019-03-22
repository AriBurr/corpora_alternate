from django.db import models

from apps.languages.models import Language

class Word(models.Model):
    word = models.TextField(unique=True)
    length = models.IntegerField(db_index=True)
    count = models.IntegerField(db_index=True)
    frequency = models.FloatField(null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.word
    
    objects = models.Manager()