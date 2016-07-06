from scrapy.item import Item, Field


class TempoagoraItem(Item):
    temperature = Field()
    sensation = Field()
    wind_velocity = Field()
    pression = Field()
    moisture = Field()
    visibility = Field()
