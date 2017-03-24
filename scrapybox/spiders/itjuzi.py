# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapybox.items import InvestEvent
import scrapy


class ItjuziSpider(CrawlSpider):
    name = "itjuzi"

    def __init__(self, rule, page_limit=2):
        self.rule = rule
        self.page_limit = page_limit
        self.name = rule.name
        self.allowed_domains = rule.allow_domains.split(",")
        self.start_urls = rule.start_urls.split(",")
        super(ItjuziSpider, self).__init__()

    def parse(self, response):
        self.page_limit -= 1
        item = InvestEvent()
        lis = response.xpath(self.rule.extract_content)
        for li in lis:
            item['publish'] = li.xpath(self.rule.publish_xpath).extract_first()
            item['company'] = li.xpath(self.rule.company_xpath).extract_first()
            investfirm = []
            investfirm_xpaths = self.rule.investfirm_xpath.split(',')
            for ixpath in investfirm_xpaths:
                investfirm = li.xpath(ixpath).extract()
                if len(investfirm) != 0: break
            item['investfirm'] = ','.join(investfirm)
            item['round'] = li.xpath(self.rule.round_xpath).extract_first()
            yield item

        if self.rule.next_page is not None and self.page_limit != 0 :
            next_page = response.xpath(self.rule.next_page).extract_first()
            yield scrapy.Request(next_page)
