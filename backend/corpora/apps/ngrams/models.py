from django.db import models

from apps.languages.models import Language

class NGram(models.Model):
    ngram_start = models.TextField(db_index=True)
    ngram_end = models.TextField()
    count = models.IntegerField()
    frequency = models.FloatField(null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, db_index=True)
    class Meta:
        unique_together = ('ngram_start', 'ngram_end')
    
    def __str__(self):
        return self.ngram_start + " " + self.ngram_end
    
    objects = models.Manager()