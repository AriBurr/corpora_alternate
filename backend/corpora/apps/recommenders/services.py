import itertools
from django.db import connection

class RecommenderService(object):
    @staticmethod
    def get_all_permutations(data):
        return [[''.join(p)] for p in itertools.permutations(data["str"], data["num"])]
        
    @staticmethod
    def search_substrings(subsrings, data):
        with connection.cursor() as cursor:
            create_temp_table = "CREATE TEMPORARY TABLE patterns (pattern VARCHAR(20));"
            insert_patterns = "INSERT INTO patterns VALUES (%s);"
            return_strings = f"SELECT word, p.pattern, count FROM words_word JOIN patterns p ON (words_word.word LIKE '%' || p.pattern || '%') WHERE length={data['length']} ORDER BY frequency DESC LIMIT 10"
            delete_temp_table = "DROP TABLE patterns"
            cursor.execute(create_temp_table)
            cursor.executemany(insert_patterns, subsrings)
            cursor.execute(return_strings)
            response = cursor.fetchall()
            cursor.execute(delete_temp_table)
            cursor.close()
            return response
