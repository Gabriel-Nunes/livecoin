# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoinwatch.com']
    start_urls = ['https://www.livecoinwatch.com']
    
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get("https://www.livecoinwatch.com")
        
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(4)
        
        self.html = driver.page_source
        self.resp = Selector(text=self.html)
        driver.close()

    def parse(self, response):
        for currency in self.resp.xpath("//tbody/tr"):
            yield {
                'Coin': currency.xpath(".//td[2]/a/div/div[contains(@class, 'item-name')]/small/text()").get(),
                'Price': currency.xpath(".//td[3]/text()[2]").get(),
                'Liquidity': currency.xpath(".//td[6]/text()").get(),
                'Market_Cap': currency.xpath(".//td[4]/text()").get(),
                'Volume(24h)': currency.xpath(".//td[5]/text()").get(),
                'All_time': currency.xpath(".//td[7]/text()").get()
            }
