# -*- coding: utf-8 -*-
import scrapy
import re

class NeruipsScheduleSpider(scrapy.Spider):
    name = 'neruips_schedule'
    allowed_domains = ['neurips.cc/Conferences/2019', 'papers.nips.cc']
    start_urls = ['https://neurips.cc/Conferences/2019/Schedule/']

    def parse(self, response):

        print("procesing:"+response.url)
        # Extracting the content using css selectors
        # from 'neurips.cc/Conferences/2019'
        types = response.css('.maincardType::text').extract()
        authors = response.css('.maincardFooter::text').extract()
        titles = response.css('.maincardBody::text').extract()
        times = response.css('.maincardHeader::text').extract()
        parent_sessions = response.css('.pull-right.maincardHeader.maincardType a::attr(href)').extract()
        ids = response.css('#main .col-xs-12.col-sm-9 div:nth-child(n+3)::attr(onclick)').extract()

        # from 'papers.nips.cc'
        abstracts = response.css('.abstract::text').extract()
        subTitle = response.css('.subtitle::text').extract()

        paper_info = {
            'abstract': abstracts[0],
            'subTitle': subTitle,
        }
        #yield or give the scraped paper info to scrapy
        yield paper_info

        #Give the extracted content row wise
        for item in zip(types, authors, titles, times, parent_sessions, ids):
            #create a dictionary to store the scraped info
            scraped_info = {
                'type': item[0],
                'author': item[1],
                'title': item[2],
                'time': item[3],
                'parent_session': item[4],
                'id': re.search(r'\((.*?)\)',item[5]).group(1),
            }

            #yield or give the scraped info to scrapy
            yield scraped_info

            NEXT_PAGE_SELECTOR = '#maincard_' + scraped_info['id'] + ' a.href_PDF::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)

    # def parsePaperPage(self, response):
    #
    #     print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    #     print("procesing:"+response.url)
    #     abstracts = response.css('.abstract::text').extract()
        #
        # #Give the extracted content row wise
        # for item in zip(types, authors, titles, times, parent_sessions, ids):
        #     #create a dictionary to store the scraped info
        #     scraped_info = {
        #         'type': item[0],
        #         'author': item[1],
        #         'title': item[2],
        #         'time': item[3],
        #         'parent_session': item[4],
        #         'id': re.search(r'\((.*?)\)',item[5]).group(1),
        #     }
        #
        #     #yield or give the scraped info to scrapy
        #     yield scraped_info
