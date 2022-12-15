from bs4 import BeautifulSoup
import urllib.request


class Parser:
    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path


    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news_s = self.html.find_all('li', class_='visible')

        for A in news_s:
            title1 = A.find('a').get_text(strip=True)  # все статьи сверху
            desc1 = A.find('time').get_text(strip=True)  # time
            href1 = A.a.get('href')  # ссылки
            self.results.append({
                'title': title1,
                'desc': desc1,
                'href': href1,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for A in self.results:
                f.write(f'\n\nНазвание:{A["title"]}\nОписание: {A["desc"]}\nСсылка: {A["href"]}\n\n********************\n')
                i += 1


    def run(self):
        self.get_html()
        self.parsing()
        self.save()