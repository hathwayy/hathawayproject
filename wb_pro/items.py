# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WbProItem(scrapy.Item):
    # define the fields for your item here like:
    user = scrapy.Field()
    fansCount = scrapy.Field()
    followCount = scrapy.Field()
    transferCount = scrapy.Field()
    pass
