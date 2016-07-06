from scrapy.spider import Spider
from scrapy.selector import Selector

from tempoagora.items import TempoagoraItem


class WeatherSpider(Spider):
    name = "weather"
    allowed_domains = ["tempoagora.com.br"]
    start_urls = (
        'http://www.tempoagora.com.br/previsao-do-tempo/sc/Criciuma/',
    )

    def parse(self, response):
        sel = Selector(response)
        resources = sel.css('ul.day-info > li > .item > span:nth-child(3)::text')
        items = []

        item = TempoagoraItem()
        item['temperature'] = resources[0].extract()
        item['sensation'] = resources[1].extract()
        item['wind_velocity'] = resources[2].extract()
        item['pression'] = resources[3].extract()
        item['moisture'] = resources[4].extract()
        item['visibility'] = resources[5].extract()
        items.append(item)
        return items
