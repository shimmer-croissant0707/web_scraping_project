from scrapy import Spider, Request
from xiachufang.items import XiachufangItem
import re

class XiachufangSpider(Spider):
    name = 'xiachufang_spider'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['https://www.xiachufang.com/category/731/pop/']

    def parse(self, response):
        num_pages = 10
        #pork_list
        # category_list = [731,227,792,1304,423,580,3297,733,5374,735,898,883,2618,2190,865,220,333,876,742,1003189]
        #chicken_list
        # category_list = [1261,5391,1509,1337,1136,1222,1227,570,393,278,1131,3155,1127,738]
        #beef_list
        # category_list = [1445,612,938,2629,5375,5403,2915,479,808,908,715,1012245]
        #lamb_list
        # category_list = [674, 145, 3249, 156, 1243]
        #duck_list
        # category_list = [1190, 274, 115, 374, 533, 714, 2653, 4068, 271, 1081, 277, 1012232]
        #fish_list
        # category_list = [5404, 5448, 523, 3042, 427, 5152]
        #shrimp_list
        # category_list = [826, 875, 1053, 1191, 41, 2918, 5322, 76, 3362, 3402, 1002, 1024, 2714, 215, 1159, 1007968]
        #egg_list
        # category_list = [394, 441, 689, 292, 4389, 1007600]
        #tofu_list
        category_list = [80, 1405, 177, 730, 947, 315, 5446, 1005208, 1000426]
        category_page = []
        for category in category_list:
            for _ in range(num_pages):
                category_page.append((category, _+1))

        # List comprehension to construct all the urls
        url_list = ['https://www.xiachufang.com/category/{0}/pop/?page={1}'.format(x[0],x[1]) for x in category_page]

        # Yield the requests to different search result urls, 
        # using parse_result_page function to parse the response.
        for url in url_list:
            yield Request(url=url, callback=self.parse_result_page)


    def parse_result_page(self, response):
        # This fucntion parses the search result page.
        
        # We are looking for url of the detail page.
        recipes = response.xpath('//div[@class="info pure-u"]')[:20]
        for recipe in recipes:
            try:
                title = recipe.xpath('.//p[@class="name"]/a/text()').extract()[0].strip()
                ingredients = recipe.xpath('.//p[@class="ing ellipsis"]/a/text()').extract()
                rating = recipe.xpath('.//p[@class="stats"]/span/text()').extract()[0]
                num_tried = recipe.xpath('.//p[@class="stats"]/span/text()').extract()[1]
                if int(num_tried) < 100:
                    break
                if recipe.xpath('.//p/i[@class="exclusive-icon ml5"]').extract_first() is not None:
                    exclusive = True
                else:
                    exclusive = False
                if recipe.xpath('.//p/i[@class="step-icon ml5"]').extract_first() is not None:
                    picture = True
                else:
                    picture = False
                author = recipe.xpath('.//p[@class="author"]/a/text()').extract()[0]
                if recipe.xpath('.//p/a[contains(@href,"/feature/cook/master/")]').extract_first() is not None:
                    master = True
                else:
                    master = False


            except:
                continue

            item = XiachufangItem()
            item['title'] = title
            item['rating'] = rating
            item['ingredients'] = ingredients
            item['num_tried'] = num_tried
            item['exclusive'] = exclusive
            item['picture'] = picture
            item['author'] = author
            item['master'] = master
            yield item





    
