import scrapy
#from ..items import WebcrawlItem

class WebcrawlSpiderSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        "https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1599617159&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0"
     ]
     
    def parse(self, response):
        #items = WebcrawlItem()

        books = response.css('span.a-size-medium.a-color-base.a-text-normal::text').extract()
        price = response.css('span.a-price-whole::text').extract()
        #items['product_name'] = product_name
        #items['product_price'] = product_price
        #yield items
        yield {
            'books':books,
            'price':price

        }
    