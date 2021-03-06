# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from socrata.items import SocrataItem


class OpendataSpider(CrawlSpider):
    name = 'opendata_crawl'
    allowed_domains = ['opendata.socrata.com']
    start_urls = ['http://opendata.socrata.com/']
    rules = [Rule(LinkExtractor(allow='browse\?&page=\d*'), callback='parse_item', follow=True)]

    def parse_item(self, response):
        titles = Selector(response).xpath('//div[@class="browse2-result"]')
        for title in titles:
            item = SocrataItem()
            item["text"] = title.xpath('.//div[@class="browse2-result-title"]/h2/a/text()').extract()[0]
            item["url"] = title.xpath('.//div[@class="browse2-result-title"]/h2/a/@href').extract()[0]
            item["views"] = title.xpath('.//div[@class="browse2-result-view-count-value"]/text()').extract()[0].strip()
            yield item

