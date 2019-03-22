import os
import urllib.request

from bs4 import BeautifulSoup
import magic
from PyPDF2 import PdfFileReader

from apps.characters.services import CharacterService
from apps.ngrams.services import NGramService
from apps.words.services import WordService

class URLUploadService(object):
    @staticmethod
    def parse_url(data):
        url = data["url"]
        language_id = data["language_id"]
        with urllib.request.urlopen(url) as response:
            stripped = response.read().decode("utf-8")
            tree = BeautifulSoup(stripped, "html.parser")
            body = tree.body
        for tag in body.select('script'):
            tag.decompose()
        for tag in body.select('style'):
            tag.decompose()
        text = body.get_text().strip()
        CharacterService.count_vectorizer(text, language_id)
        WordService.count_vectorizer(text, language_id)
        NGramService.count_vectorizer(text, language_id)

class FileUploadService:
    @staticmethod
    def parse_file_type(data):
        language_id = data["language_id"]
        path = "media"
        file_list = os.listdir(path)
        for i in file_list:
            file_type = magic.from_file(f'media/{i}').split(", ")
            if file_type[0] == "ASCII text" or file_type[0] == "Rich Text Format data" or file_type[0] == "UTF-8 Unicode text":
                FileUploadService.convert_ASCII(i, language_id)
            elif file_type[0] == "PDF document":
                FileUploadService.convert_PDF(i, language_id)
        FileUploadService.remove_media_file()    

    @staticmethod
    def convert_ASCII(file,language_id):
        document = open(f'media/{file}', 'rb')
        text = document.read().decode("utf-8")
        CharacterService.count_vectorizer(text, language_id)
        WordService.count_vectorizer(text, language_id)
        NGramService.count_vectorizer(text, language_id)

    @staticmethod
    def convert_PDF(file,language_id):
        with open(f'media/{file}', 'rb') as text_file:
            pdf = PdfFileReader(text_file)
            if pdf.isEncrypted:
                pdf.decrypt('')
            number_of_pages = pdf.getNumPages()
            for page_number in range(number_of_pages):
                page = pdf.getPage(page_number)
                text = page.extractText()
                CharacterService.count_vectorizer(text, language_id)
                WordService.count_vectorizer(text, language_id)
                NGramService.count_vectorizer(text, language_id)
    
    @staticmethod
    def remove_media_file():
        path = "media"
        file_list = os.listdir(path)
        for i in file_list:
            os.remove(f'media/{i}')