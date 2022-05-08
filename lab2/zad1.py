import scrapy


class NewsSpider(scrapy.Spider):
    name = "zad1"
    start_urls = [
        "https://wiadomosci.onet.pl/swiat/wojna-rosja-ukraina-wywiad-bialorus-moze-przystapic-do-wojny/vepk97d"
    ]

    def parse(self, response):
        print("tmp")
        title = response.xpath('/html/body/section/article/section[1]/section/div/header/h1/text()').get()
        print(title)

    """
        Plik robots.txt ogranicza dostep do zawartosci strony robotom
        wyszukiwarek. Plik na stronie Onet pozwala indeksowac cala zawartosc
        strony.
    """
