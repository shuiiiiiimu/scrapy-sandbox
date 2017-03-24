# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyboxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class InvestEvent(scrapy.Item):
    company = scrapy.Field()
    investfirm = scrapy.Field()
    round = scrapy.Field()
    publish = scrapy.Field()
    pass