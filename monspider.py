import scrapy


class MonspiderSpider(scrapy.Spider):
    name = "monspider"
    allowed_domains = ["www.welcometothejungle.com"]
    start_urls = ["https://www.welcometothejungle.com/fr"]

    def parse(self, response):
        pass
