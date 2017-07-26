import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from konachan.spiders.image_spider import ImageSpider

process = CrawlerProcess(get_project_settings())
process.crawl(ImageSpider())
process.crawl(ImageSpider(start=3200))
process.crawl(ImageSpider(start=6200))
process.start()