import scrapy


class LightparsSpider(scrapy.Spider):
    name = "lightpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css("div._Ud0k")
        for light in lights:
            yield {
                "name": light.css("div.lsooF span::text").get(),
                "price": light.css("div.pY3d2 span::text").get(),
                "url": light.css("a::attr(href)").get(),

            }