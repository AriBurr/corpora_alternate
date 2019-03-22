from django.db import models

from apps.languages.models import Language
from apps.words.models import Word

class NGram(models.Model):
    word_one = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='ngram_word_one', null=True)
    word_two = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='ngram_word_two', null=True)
    word_three = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='ngram_word_three', null=True)
    count = models.IntegerField()
    frequency = models.FloatField(null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    class Meta:
        unique_together = ('word_one', 'word_two', 'word_three')
    
    objects = models.Manager()