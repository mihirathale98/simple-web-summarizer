import re
import bs4
import requests


class Scraper:
    def __init__(self):
        ## define patterns
        self.hyperlink_pattern = r'https?:\/\/\S+'

    
    def get_web_body(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def parse_web_body(self, web_body):
        soup = bs4.BeautifulSoup(web_body, 'html.parser')
        return soup

    def get_text_from_soup(self, soup):
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text


    def get_text_from_url(self, url):
        web_body = self.get_web_body(url)
        soup = self.parse_web_body(web_body)
        text = self.get_text_from_soup(soup)
        text = self.clean_text(text)
        return text


    def clean_text(self, text):
        text = self.remove_hyperlinks(text)
        return text

    def remove_hyperlinks(self, text):
        return re.sub(self.hyperlink_pattern, '', text)
