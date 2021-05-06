import scrapy
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class DataSpider(scrapy.Spider):
    name = 'Data'
    allowed_domains = ['']
    start_urls = ['']

    def __init__(self , *args , **kargs):
    	self.start_urls=["https://www.google.com"]
    	self.driver = webdriver.Chrome(executable_path='E://gunjan//chromedriver.exe')


    def parse(self, response):
    	actions = ActionChains(self.driver)
    	self.driver.get('https://store.hp.com/us-en/shop/pdp/hp-laptop-14z-fq1000-touch-optional-2j9v5av-1')
    	time.sleep(10)

    	self.driver.maximize_window()

    	button = self.driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
    	time.sleep(10)
    

    	response = scrapy.Selector(text=self.driver.page_source)

    	try:
    		try:
    			btn = self.driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/button').click()
    		
    		except:
    			btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/button').click()
    		
    		time.sleep(5)

    		title = response.xpath('//div[@class="product-detail"]/h1/text()').extract()
	    	print(title)

	    	# hero_text = response.xpath('//*[@id="content"]/div[1]/div[2]/div[2]/div/ul/li[2]/text()').extract()
	    	hero_text = response.xpath('//ul[@class="ksps"]//li[2]/text()').extract()
	    	print(hero_text)

	    	btn = self.driver.find_element_by_xpath('//*[@id="tab_1"]').click()

	    	time.sleep(5)

	    	
	    	product_text= self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]').text
	    	print(product_text)

    	except:

	    	title = response.xpath('//div[@class="product-detail"]/h1/text()').extract()
	    	print(title)

	    	# hero_text = response.xpath('//*[@id="content"]/div[1]/div[2]/div[2]/div/ul/li[2]/text()').extract()
	    	hero_text = response.xpath('//ul[@class="ksps"]//li[2]/text()').extract()
	    	print(hero_text)

	    	btn = self.driver.find_element_by_xpath('//*[@id="tab_1"]').click()

	    	time.sleep(5)

	    	
	    	product_text = self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]').text
	    	print(product_text)


	    	for i in response.xpath('//div[contains(@class,"specs-cell spec-values")]/text()'):
	    		print(i.extract())






        
