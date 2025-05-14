import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svetilniks = response.css('div._Ud0k')
        for svetilnik in svetilniks:
            yield {
                'name': svetilnik.css('div.lsooF span::text').get(),
                'price': svetilnik.css('div.pY3d2 span.ui-LD-ZU::text').get(),
                'url': svetilnik.css('div.lsooF a::attr(href)').get(),
             }
