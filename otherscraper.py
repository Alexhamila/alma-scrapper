import scrapy
import json


class EmissionsSpider(scrapy.Spider):
    name = "emissions"
    url_numb = 1
    changeUrl = 'https://www.almaclindoeilfm.org/emissions?page='+str(url_numb)
    start_urls = [
        changeUrl
    ]

    def parse(self, response):
        SET_SELECTOR = '.views-row'
        number = 0
        item = 0
        for emission in response.css(SET_SELECTOR):
            if number <= 9:
                NAME_SELECTOR = 'div div span a ::text'
                LINK_SELECTOR = 'div div span a::attr(href)'
                yield{
                    'Titre': emission.css(NAME_SELECTOR).extract_first(),
                    'Link' : emission.css(LINK_SELECTOR).extract_first(),
                    'ID': item,
                }
                number += 1
                item +=1
    url_numb +=1
