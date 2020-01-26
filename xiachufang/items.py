# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiachufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    num_tried = scrapy.Field()
    picture = scrapy.Field()
    exclusive = scrapy.Field()
    ingredients = scrapy.Field()
    author = scrapy.Field()
    master = scrapy.Field()

