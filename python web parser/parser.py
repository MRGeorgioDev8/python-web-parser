import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open("it_world.csv", "a") as f:
        write = csv.writer(f, delimiter=";", lineterminator="\n")
        write.writerow((data['name'], data['url'], data['date']))

def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    connected = soup.find_all("div", class_="news-list news__content")
    for connected in connected:
        try:
            name = connected.find("h2").text.strip()
        except ValueError:
            name = ""

        url = connected.find("div").find("a")["href"]
        date = connected.find("span", class_="color-silver").text.strip()
        data = {'name': name, "url": url, "date": date}
        write_csv(data)

def main():
    url = "https://www.it-world.ru/news-company/releases/"
    get_data(get_html(url))

if __name__ == '__main__':
    main()