import scrapy


class NewsSpider(scrapy.Spider):
    name = "zad2"
    start_urls = [
        "https://gazetawroclawska.pl/"
    ]

    def parse(self, response):

        links = response.xpath('//a[@class = "atomsListingArticleTile__img"]/@href').extract()
        titles = response.xpath('//a[@class = "atomsListingArticleTile__img"]/@title').extract()
        print(links)
        print(titles)

    """
        Opoznienie wprowadza sie, zeby strona nie uznala naszej aplikacji za
        atak. W tym wypadku wyciagam tytuly z linku, wiec go nie wprowadzam.
    """
