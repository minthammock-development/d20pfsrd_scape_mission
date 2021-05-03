import scrapy
import time


class ItemSpider(scrapy.Spider):
  name = "items"

  def start_requests(self):
      urls = [
          'https://www.d20pfsrd.com/magic-items/rings',
          # 'https://www.d20pfsrd.com/magic-items/staves',
          # 'https://www.d20pfsrd.com/magic-items/wands',
          # 'https://www.d20pfsrd.com/magic-items/wondrous-items',
          # 'https://www.d20pfsrd.com/magic-items/artifacts',
          # 'https://www.d20pfsrd.com/magic-items/intelligent-items',
          # 'https://www.d20pfsrd.com/magic-items/cursed-items',
      ]
      for url in urls:
          yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
      # page = response.url.split("/")[-2]
      for href in response.css('div.ogn-childpages ul.ogn-childpages li a::attr(href)').getall():
        yield response.follow(href, callback = self.chaseLinks)
        time.sleep(.1)

  def chaseLinks(self, res):
    itemName = res.css('main h1::text').get()
    itemInfo = res.css('div.page-center p::text').getall()
    yield {
      'name' : itemName,
      'info' : itemInfo
    }