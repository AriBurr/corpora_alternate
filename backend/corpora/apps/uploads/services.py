import urllib.request
from bs4 import BeautifulSoup

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
        return body.get_text().strip()