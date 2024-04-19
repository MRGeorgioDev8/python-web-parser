import requests
from bs4 import BeautifulSoup

class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="news-item")
        for item in news:
            title = item.find("h2").text.strip()
            href = item.find("a").get("href")
            time = item.find("time", class_="news-item__date").text.strip()
            self.res.append({
                'title': title,
                'href': href,
                'time': time
            })
        print(self.res)

    def save(self):
        with open(self.path, 'w+') as f:
            i = 1
            for item in self.res:
                f.write(f"Новость # {i}\n\nНазвание: {item['title']}\nСсылка: {item['href']}\n\nДата: {item['time']}\n\n{'*' * 20}\n\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()