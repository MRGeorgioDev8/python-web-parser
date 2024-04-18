from parser_news import Parser

def main():
    pars = Parser("https://rb.ru/news/", "news.txt")
    pars.run()

if __name__ == '__main__':
    main()