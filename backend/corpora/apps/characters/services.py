from django.db import connection

from sklearn.feature_extraction.text import CountVectorizer

import re

class CharacterService(object):
    @staticmethod
    def count_vectorizer(text, language_identifier):
        alpha = re.sub(r"[^a-zA-Z]+", "", text)
        vectorizer = CountVectorizer(analyzer="char", lowercase=False)
        tokens = vectorizer.fit([alpha]).get_feature_names()
        freq = vectorizer.transform([alpha]).toarray()[0].tolist()
        lang = [language_identifier] * len(tokens)
        data = [list(t) for t in zip(tokens, freq, lang)]
        CharacterService.insert_characters(data)

    @staticmethod
    def insert_characters(data):
        print('start bulk insert chars')
        with connection.cursor() as cursor: 
          cursor.executemany(
                "INSERT INTO characters_character(character,count,language_id)\
                VALUES (%s,%s,%s) ON CONFLICT (character)\
                DO UPDATE SET count = excluded.count + characters_character.count;", data)
        cursor.close()
        print('end bulk insert chars')
    
    @staticmethod
    def update_char_freq(lang):
        print('start bulk update chars')
        with connection.cursor() as cursor: 
            cursor.execute(
                f"WITH new_values AS (SELECT id, count / (SELECT SUM(count)::FLOAT FROM characters_character) AS freq FROM characters_character WHERE language_id={lang})\
                update characters_character as old_values\
                set frequency = new_values.freq\
                from new_values new_values\
                where new_values.id = old_values.id;"    
            )    
        cursor.close()
        print('end bulk insert chars')    