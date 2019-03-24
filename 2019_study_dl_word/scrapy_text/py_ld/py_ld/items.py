# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Headline(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    ニュースのヘッドライン
    """

    title = scrapy.Field()
    body = scrapy.Field()