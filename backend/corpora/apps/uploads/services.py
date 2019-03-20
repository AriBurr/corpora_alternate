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
    def parse_url(url):
        with urllib.request.urlopen(url) as response:
            stripped = response.read().decode("utf-8")
            tree = BeautifulSoup(stripped, "html.parser")
            body = tree.body
        for tag in body.select('script'):
            tag.decompose()
        for tag in body.select('style'):
            tag.decompose()
        text = body.get_text().strip()
        CharacterService.count_vectorizer(text)
        NGramService.count_vectorizer(text)
        WordService.count_vectorizer(text)

class FileUploadService:
    @staticmethod
    def parse_file_type():
        path = "media"
        file_list = os.listdir(path)
        for i in file_list:
            file_type = magic.from_file(f'{i}').split(", ")
            if file_type[0] == "ASCII text" or file_type[0] == "Rich Text Format data":
                FileUploadService.convert_ASCII(i)
            elif file_type[0] == "PDF document":
                FileUploadService.convert_PDF(i)
        FileUploadService.remove_media_file()    

    @staticmethod
    def convert_ASCII(file):
        document = open(f'media/{file}', 'rb')
        text = document.read().decode("utf-8")
        CharacterService.count_vectorizer(text)
        NGramService.count_vectorizer(text)
        WordService.count_vectorizer(text)

    @staticmethod
    def convert_PDF(file):
        with open(f'media/{file}', 'rb') as text_file:
            pdf = PdfFileReader(text_file)
            if pdf.isEncrypted:
                pdf.decrypt('')
            number_of_pages = pdf.getNumPages()
            for page_number in range(number_of_pages):
                page = pdf.getPage(page_number)
                text = page.extractText()
                CharacterService.count_vectorizer(text)
                NGramService.count_vectorizer(text)
                WordService.count_vectorizer(text)
    
    @staticmethod
    def remove_media_file():
        path = "media"
        file_list = os.listdir(path)
        for i in file_list:
            os.remove(f'media/{i}')