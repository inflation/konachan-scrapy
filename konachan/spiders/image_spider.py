import scrapy


class ImageSpider(scrapy.Spider):
  name = "image"
  start_urls = [
      "http://konachan.net/post?page=1&tags=",
  ]

  def parse(self, response):
    for href in response.css('.thumb::attr(href)').extract():
      yield scrapy.Request(response.urljoin(href), callback=self.parse_detail)

    next_page = response.css('a.next_page::attr(href)').extract_first()
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, callback=self.parse)

  def parse_detail(self, response):
    yield {
        'image_urls': [response.urljoin(response.css('.image::attr(src)').extract_first())],
    }
