import scrapy


class CarscraperSpider(scrapy.Spider):
    name = 'carscraper'
    allowed_domains = ['bonbanh.com']
    page_number = 1
    start_urls = ['http://bonbanh.com/oto/page,2']

    def parse(self, response):
        #items1 = {'Name':[], 'Condition':[], 'Price':[], 'Location':[], 'Link':[],'ODO':[], 'Car_code':[]}
        for cars in response.css('li.car-item.row1'):
            yield   {
                    'Name': cars.css('h3[itemprop="name"]::text').get(),
                    'Condition': cars.css('div.cb1::text').get(),
                    'Price' : cars.css('b[itemprop="price"]::text').get(),
                    'Location' : cars.css('div.cb4 > b ::text').get(),
                    'Link' : cars.css('a[itemprop="url"]').attrib['href'],
                    'ODO' : cars.css('span.inp::text').get(),
                    'Car_code' : cars.css('span.car_code::text').get()
                    }
        for cars in response.css('li.car-item.row2'):
            yield   {
                    'Name': cars.css('h3[itemprop="name"]::text').get(),
                    'Condition': cars.css('div.cb1::text').get(),
                    'Price' : cars.css('b[itemprop="price"]::text').get(),
                    'Location' : cars.css('div.cb4 > b ::text').get(),
                    'Link' : cars.css('a[itemprop="url"]').attrib['href'],
                    'ODO' : cars.css('span.inp::text').get(),
                    'Car_code' : cars.css('span.car_code::text').get()
                    }
        next_page = 'http://bonbanh.com/oto/page,' + str(CarscraperSpider.page_number)
        if CarscraperSpider.page_number < 1995:
            CarscraperSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

        pass
