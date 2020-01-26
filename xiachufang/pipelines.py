# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exporters import CsvItemExporter


class WriteItemPipeline(object):

    def __init__(self):
        # self.filename = 'xiachufang_pork.csv'
        # self.filename = 'xiachufang_chicken.csv'
        # self.filename = 'xiachufang_beef.csv'
        # self.filename = 'xiachufang_lamb.csv'
        # self.filename = 'xiachufang_duck.csv'
        # self.filename = 'xiachufang_fish.csv'
        # self.filename = 'xiachufang_shrimp.csv'
        # self.filename = 'xiachufang_egg.csv'
        self.filename = 'xiachufang_tofu.csv'

    def open_spider(self, spider):
        self.csvfile = open(self.filename, 'wb')
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
