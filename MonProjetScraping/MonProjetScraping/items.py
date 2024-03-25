# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MonprojetscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quote = scrapy.Field()
    author = scrapy.Field()
    about = scrapy.Field()
    tags = scrapy.Field()
    pass
