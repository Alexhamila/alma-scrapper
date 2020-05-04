import scrapy
import json


class EmissionsSpider(scrapy.Spider):
    name = "emissions"
    url_numb = 1
    changeUrl = 'https://www.almaclindoeilfm.org/emissions?page='+str(url_numb)

    def start_requests(self):
        yield scrapy.Request(url=changeUrl, callback=self.parse_data)
    
    def parse_data(self, response):
        SET_SELECTOR = '.views-row'
        number = 0
        item = 0
        for emission in response.css(SET_SELECTOR):
            if number <= 9:
                NAME_SELECTOR = 'div div span a ::text'
                DATE_SELECTOR = '.views-field-field-date-emission div span ::text'
                CATEGORIE_SELECTOR = '.views-field-field-cat-gorie div ::text'
                yield{
                    'Titre': emission.css(NAME_SELECTOR).extract_first(),
                    'Date': emission.css(DATE_SELECTOR).extract_first(),
                    'Categorie': emission.css(CATEGORIE_SELECTOR).extract_first(),
                    'ID': item,
                }
                number += 1
                item +=1
        url_numb +=1
