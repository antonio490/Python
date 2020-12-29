import scrapy


class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['www.idealista.com']

    def start_requests(self):

    def parse(self, response):
        pass
