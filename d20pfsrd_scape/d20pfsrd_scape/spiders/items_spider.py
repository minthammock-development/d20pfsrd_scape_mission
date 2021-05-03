import scrapy
import time


class ItemSpider(scrapy.Spider):
  name = "items"

  def start_requests(self):
      urls = [
          'https://www.d20pfsrd.com/magic-items/rings',
          'https://www.d20pfsrd.com/magic-items/staves',
          'https://www.d20pfsrd.com/magic-items/wands',
          'https://www.d20pfsrd.com/magic-items/wondrous-items',
          'https://www.d20pfsrd.com/magic-itemsartifacts',
          'https://www.d20pfsrd.com/magic-items/intelligent-items',
          'https://www.d20pfsrd.com/magic-items/cursed-items',
      ]
      for url in urls:
          yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
      # page = response.url.split("/")[-2]
      hrefs = response.css('li.page\ new\ parent a::attr(href)').getall()
      yield from response.follow_all(hrefs, callback = self.chaseLinks)

  def chaseLinks(self, response):
    yield 
    {
      'html' : response.body
    }
    time.sleep(.3)


  filename = f'quotes-{page}.json'
  with open(filename, 'wb') as f:
      f.write(response.body)
  self.log(f'Saved file {filename}')