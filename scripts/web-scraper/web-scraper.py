#!/usr/bin/env python3
import requests
from html.parser import HTMLParser
import sys
import json
from urllib.parse import urljoin, urlparse

class SimpleScraper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.texts = []
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.links.append(value)
        if tag in ['script', 'style']:
            self.current_text = []

    def handle_data(self, data):
        text = data.strip()
        if text:
            self.current_text.append(text)

    def handle_endtag(self, tag):
        if tag in ['p', 'h1', 'h2', 'h3', 'li']:
            if self.current_text:
                self.texts.append(' '.join(self.current_text))
                self.current_text = []

def scrape(url):
    resp = requests.get(url, timeout=10, headers={'User-Agent': 'SimpleScraper/1.0'})
    scraper = SimpleScraper()
    scraper.feed(resp.text)
    return {
        'url': url,
        'links': [urljoin(url, l) for l in scraper.links[:50]],
        'texts': scraper.texts[:30]
    }

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://example.com'
    result = scrape(url)
    print(json.dumps(result, indent=2, ensure_ascii=False))
