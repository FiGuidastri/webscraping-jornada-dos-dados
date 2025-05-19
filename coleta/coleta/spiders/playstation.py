import scrapy


class PlaystationSpider(scrapy.Spider):
    name = "playstation"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/ps5#D[A:ps5]"]

    def parse(self, response):
        
        products = response.css('div.ui-search-result__wrapper')

        for product in products:

            prices = product.css('span.andes-money-amount__fraction::text').getall()

            yield {
                'brand': product.css('span.poly-component__brand::text').get(), # trás o nome da marca
                'title': product.css('a.poly-component__title::text').get(), # trás o nome do produto
                'seller': product.css('span.poly-component__seller::text').get(), # trás o nome do vendedor
                'old_price': prices[0] if len (prices) > 0 else None, # trás o preço do produto
                'new_price': prices[1] if len (prices) > 0 else None, # trás o preço do produto
            }