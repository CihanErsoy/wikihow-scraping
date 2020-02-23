import scrapy
from ..items import WikItem
from urllib.parse import urljoin

class WikwikSpider(scrapy.Spider):
    name = 'wikwik'
    allowed_domains = ['wikihow.com.tr']
    start_urls = ['https://www.wikihow.com.tr/Kategori:E%C4%9Fitim-ve-%C4%B0leti%C5%9Fim']
    def parse(self, response):
        all_contents = response.xpath('//*[@class="thumbnail s-height s-width"]')
        for content in all_contents:
            link = content.xpath('./a/@href').get()
            yield response.follow(url = link, callback = self.parse_pages)
        next_page =  response.xpath('//*[@id="cat_all"]/a[2]/@href').get()
        yield response.follow(url = urljoin('https://www.wikihow.com.tr', next_page), callback=self.parse)

    def parse_pages(self, response):
        data = WikItem()
        article=' '
        data['title'] = response.xpath('//h1[contains(@class, "firstHeading")]/a/text()').get()
        p_list = response.xpath('//div[@class="step"]/descendant::text()').getall()
        for p in p_list:
            if p == '\n':
                pass
            else:
                article = article + p
        data['article']=article
        yield data
