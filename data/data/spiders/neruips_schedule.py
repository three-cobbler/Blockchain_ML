# -*- coding: utf-8 -*-
import scrapy


class NeruipsScheduleSpider(scrapy.Spider):
    name = 'neruips_schedule'
    allowed_domains = ['neurips.cc/Conferences/2019']
    start_urls = ['https://neurips.cc/Conferences/2019/Schedule/']

    def parse(self, response):
        # Extracting the content using css selectors
        types = response.css('.maincardType::text').extract()
        authors = response.css('.maincardFooter::text').extract()
        titles = response.css('.maincardBody::text').extract()
        times = response.css('.maincardHeader::text').extract()
        parent_sessions = response.css('.pull-right.maincardHeader.maincardType a::attr(href)').extract()
        # abstracts = response.css('.abstract::text').extract()

        #Give the extracted content row wise
        for item in zip(types,authors,titles,times,parent_sessions):
            #create a dictionary to store the scraped info
            scraped_info = {
                'type': item[0],
                'author': item[1],
                'title': item[2],
                'time': item[3],
                'parent_session': item[4],
                # 'abstract': item[5],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info


            # NEXT_PAGE_SELECTOR = '.maincardType + a::attr(href)'
            # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            # if next_page:
            #     yield scrapy.Request(
            #     response.urljoin(next_page),
            #     callback=self.parse)
