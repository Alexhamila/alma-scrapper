import scrapy
import json

class EmissionsPageSpider(scrapy.Spider):
    name = "emissions"
    start_urls = ['https://www.almaclindoeilfm.org/emissions?page=1']
    def parse(self, response):
        number = 0
        SET_SELECTOR = '.views-row'
        for emission_url in response.css(SET_SELECTOR):
            if(number < 10):
                item = ""
                url = emission_url.css('div div span a ::attr("href")').extract_first()
                NAME_SELECTOR = 'div div span a ::text'
                DATE_SELECTOR = '.views-field-field-date-emission div span ::text'
                CATEGORIE_SELECTOR = '.views-field-field-cat-gorie div ::text'
                yield response.follow(url, callback=self.parse_emission, 
                    meta={
                    'Titre': emission_url.css(NAME_SELECTOR).extract_first(),
                    'Date': emission_url.css(DATE_SELECTOR).extract_first(),
                    'Categorie': emission_url.css(CATEGORIE_SELECTOR).extract_first(),
                    'Lien' : "https://www.mixcloud.com/cedric-clindoeilfm/"+ url[9:]})
                    
                number+=1
        next_page = response.css('.pager-next a').attrib['href']
        next_page = response.urljoin(next_page)
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
    
    def parse_emission(self, response):
        titre = response.meta.get('Titre')
        date = response.meta.get("Date")
        categorie = response.meta.get("Categorie")
        lien = response.meta.get("Lien")
        description = response.css('.field-item div::text').extract_first()
        yield {
            "Titre": titre,
            "Date": date,
            "Categorie": categorie,
            "Lien": lien,
            "Description": description,
        }