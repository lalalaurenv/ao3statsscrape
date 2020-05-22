# -*- coding: utf-8 -*-
import scrapy
from ao3scrape.items import Ao3ScrapeItem #to be able to store the results in a useable output
import datetime #to be able to get the date

class ProfilescraperSpider(scrapy.Spider):
    name = "profilescraper" #the name of the spider
    
    #the URLs where the spider will go
    allowed_domains = ["archiveofourown.org"]
    start_urls = ['https://archiveofourown.org/users/YOURUSERNAME/works'] #PUT YOUR PROFILE URL HERE

#parse function. the content of the scraped URL is passed on as the response object
    def parse(self, response):
        for url in response.xpath("//h4//a[not(@rel)]/@href").extract():
        #    print(response.urljoin(url))
            full_url = response.urljoin(url)
            full_url = full_url + '?view_adult=true'
            print("Found URL: " + full_url)
            yield scrapy.Request(full_url, callback=self.get_details)

    def get_details(self, response):
    #make a new item object to store all the details about the fics
        item = Ao3ScrapeItem()
    #use xpaths to extract everything and store it in the item. for some reason the title can't be pulled with xpath?
        currentdate = datetime.date.today()
        currenttime = datetime.datetime.now()
        item['crawldate'] = str(currentdate)
        item['crawltime'] = currenttime.strftime("%H:%M:%S")
        item['ficURL'] = str(response.url)
        item['ficTitle'] = response.xpath("normalize-space(//*[@id='workskin']/div[1]/h2)").getall()
        item['hits'] = response.xpath("//dd[@class='hits']//text()").extract()
        item['kudos'] = response.xpath('//dd[@class="kudos"]//text()').extract()
        item['comments'] = response.xpath("//dd[@class='comments']//text()").extract()
        item['bookmarks'] = response.xpath("//dd[@class='bookmarks']//text()").extract()
        yield item

