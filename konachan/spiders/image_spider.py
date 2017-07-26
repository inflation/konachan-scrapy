import scrapy


class ImageSpider(scrapy.Spider):
  name = "image"
  start_urls = [
      "http://konachan.net/post?page=1&tags=",
  ]

  def parse(self, response):
    yield {
        'image_urls': [response.urljoin(url) for url in 
            response.xpath('//a[contains(@class, "largeimg")]/@href').extract()]
    }

    next_page = response.xpath('//a[@class="next_page"]/@href').extract_first()
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, callback=self.parse)
