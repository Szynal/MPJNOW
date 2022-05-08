import scrapy
from time import sleep


class NewsSpider(scrapy.Spider):
    name = "zad3"
    start_urls = [
        "https://gazetawroclawska.pl/"
    ]

    def parse(self, response):

        links = response.xpath('//a[@class = "atomsListingArticleTile__img"]/@href').extract()
        for href in links:
            url = response.urljoin(href)
            yield scrapy.Request(url, callback = self.parse_dir_contents)
            sleep(2)



    def parse_dir_contents(self, response):
        item = {}
        item['title'] = response.xpath('/html/body/main/article/div/header/h1/text()').extract()
        item['time'] = response.xpath('/html/body/main/article/div/header/span/span[2]/span/time/text()').extract()
        item['author'] = response.xpath('/html/body/main/article/div/header/span/a/span/text()').extract()
        item['tags'] = response.xpath('//a[@class = "atomsTags"]/@title').extract()
        item['content'] = response.xpath('/html/body/main/article/div/div[5]/div[1]').extract()
        print(item)
        yield item
