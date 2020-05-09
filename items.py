# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ao3ScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    crawldate = scrapy.Field()
    crawltime = scrapy.Field()
    ficURL = scrapy.Field()
    hits = scrapy.Field()
    kudos = scrapy.Field()
    bookmarks = scrapy.Field()
    comments = scrapy.Field()
