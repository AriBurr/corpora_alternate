from django.db import connection

from sklearn.feature_extraction.text import CountVectorizer

class WordService(object):
    @staticmethod
    def count_vectorizer(text, language_identifier):
        vectorizer = CountVectorizer(
            token_pattern=r"\b[a-zA-Z\']+\b", analyzer="word")
        tokens = vectorizer.fit([text]).get_feature_names()
        length = [len(t) for t in tokens]
        freq = vectorizer.transform([text]).toarray()[0].tolist()
        lang = [language_identifier] * len(tokens)
        data = [list(t) for t in zip(tokens, length, freq, lang)]
        with connection.cursor() as cursor:
            cursor.executemany(
                "INSERT INTO words_word(word,length,count,language_id)\
                VALUES (%s,%s,%s,%s) ON CONFLICT (word)\
                DO UPDATE SET count = excluded.count + words_word.count;", data)
            cursor.execute(
                "WITH new_values AS (SELECT id, count / (SELECT SUM(count)::FLOAT FROM words_word) AS freq FROM words_word)\
                update words_word as old_values\
                set frequency = new_values.freq\
                from new_values new_values\
                where new_values.id = old_values.id;"
            )
            cursor.close()
