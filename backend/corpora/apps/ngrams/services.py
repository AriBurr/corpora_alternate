from django.db import connection

from sklearn.feature_extraction.text import CountVectorizer

class NGramService(object):
    @staticmethod
    def count_vectorizer(text, lang):
        vectorizer = CountVectorizer(token_pattern=r"\b[\w']+\b", analyzer="word", ngram_range=(3,3), min_df=1)
        tokens = vectorizer.fit([text]).get_feature_names() 
        freq = vectorizer.transform([text]).toarray()[0].tolist() 
        n_grams = []
        for i, t in enumerate(tokens):
            words = t.split()
            n_grams.append([words[0] + ' ' + words[1], words[2], freq[i], lang])
        with connection.cursor() as cursor: 
            cursor.executemany(  
                "INSERT INTO ngrams_ngram(ngram_start,ngram_end,count, language_id)\
                VALUES (%s,%s,%s,%s) ON CONFLICT (ngram_start, ngram_end)\
                DO UPDATE SET count = excluded.count + ngrams_ngram.count", 
                n_grams)
            cursor.execute(
                "WITH new_values AS (SELECT id, count / (SELECT SUM(count)::FLOAT FROM ngrams_ngram) AS freq FROM ngrams_ngram)\
                update ngrams_ngram as old_values\
                set frequency = new_values.freq\
                from new_values new_values\
                where new_values.id = old_values.id;"          
            )    
            cursor.close()