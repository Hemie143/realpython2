# -*- coding: utf-8 -*-
import scrapy

from realpython2.chp24_interlude_web_scraping.hacknews.hacknews.items import HacknewsItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['http://news.ycombinator.com/']

    def parse(self, response):
        titles = scrapy.selector.Selector(response).xpath('//tr[@class="athing"]/td[3]')
        for title in titles:
            item = HacknewsItem()
            item['title'] = title.xpath("a[@href]/text()").extract()
            item['url'] = title.xpath("a/@href").extract()
            yield item
