import scrapy
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time , csv


class DataSpider(scrapy.Spider):
    name = 'Data'
    allowed_domains = ['']
    start_urls = ['']
 

    def __init__(self , *args , **kargs):
    	self.start_urls=["https://www.google.com"]
    	self.driver = webdriver.Chrome(executable_path='E://gunjan//chromedriver.exe')


    def parse(self, response):
    	with open(r'C:\Users\gunjan\Downloads\amd_hp_laptop - amd_hp_laptop (1).csv', newline='') as csvfile:
    		data = csv.DictReader(csvfile)

    		links=[]
    		for row in data:
    			links.append(row['link'])
    		print(len(links))

    	actions = ActionChains(self.driver)

    	self.driver.maximize_window()

    	for url  in links:
    		self.driver.get(url)


    		time.sleep(5)

    		try:
    			button = self.driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
    			time.sleep(5)
    		except:
    			pass

    	# button = self.driver.find_element_by_xpath('//div[@class="ot-sdk-row"]')
    

    		response = scrapy.Selector(text=self.driver.page_source)
    		# print(response)
    		time.sleep(5)
    		try:
    			try:
    				btn = self.driver.find_element_by_xpath('//div[@class="oos-popup-container"]//button').click()
    			except:
    				btn = self.driver.find_element_by_xpath('//div[@class="react-modal-bg pdp-upsell-bg"]//button').click()
    			# btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/button').click()
    			time.sleep(5)

    			title = response.xpath('//div[@class="product-detail"]/h1/text()').extract()
    			print(title)

    			hero_text = response.xpath('//ul[@class="ksps"]//li[2]/text()').extract()
    			print(hero_text)

    			btn = self.driver.find_element_by_xpath('//*[@id="tab_1"]').click()
    			time.sleep(5)


    			response_body = scrapy.Selector(text=self.driver.page_source)
    			product_text = response_body.xpath("//div[@class='specs-row clearfix'][2]/div[@class='specs-cell spec-values']/div[@class='spec-value']/text()").extract_first()
    			print(product_text)

    			yield{
    			'Product_url' : url,
    			'Product_name' : title,
    			'Product_text' : product_text,
    			'Hero_text' : hero_text
			}
	    	

    		except:

    			title = response.xpath('//div[@class="product-detail"]/h1/text()').extract()
    			print(title)
    			
    			hero_text = response.xpath('//ul[@class="ksps"]//li[2]/text()').extract()
    			print(hero_text)

    			btn = self.driver.find_element_by_xpath('//*[@id="tab_1"]').click()
    			time.sleep(5)

    			response_body = scrapy.Selector(text=self.driver.page_source)
    			product_text = response_body.xpath("//div[@class='specs-row clearfix'][2]/div[@class='specs-cell spec-values']/div[@class='spec-value']/text()").extract_first()
    			print(product_text)

    			yield{
				'Product_url' : url,
				'Product_name' : title,
				'Product_text' : product_text,
				'Hero_text' : hero_text
				}
	    	

    	# except:

	    # 	title = response.xpath('//div[@class="product-detail"]/h1/text()').extract()
	    # 	# print(title)

	    # 	# hero_text = response.xpath('//*[@id="content"]/div[1]/div[2]/div[2]/div/ul/li[2]/text()').extract()
	    # 	hero_text = response.xpath('//ul[@class="ksps"]//li[2]/text()').extract()
	    # 	print(hero_text)

	    # 	btn = self.driver.find_element_by_xpath('//*[@id="tab_1"]').click()
	    # 	# btn = self.driver.find_element_by_xpath('//ul[@class="pdp-tabs-nav clearfix"]/li[2]').click()
	    # 	# btn = self.driver.find_element_by_xpath("//li[contains(@class , 'pdp-nav-tab unstyled')][1]").click()
	    # 	time.sleep(5)

	    	
	    # 	# product_text = self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]').text
	    # 	# print(product_text)

	    # 	# ab = response.xpath("//div[contains(@class , 'specs-row clearfix')]").extract()
	    # 	response_body = scrapy.Selector(text=self.driver.page_source)
	    # 	product_text = response_body.xpath("//div[@class='specs-row clearfix'][2]/div[@class='specs-cell spec-values']/div[@class='spec-value']/text()").extract_first()
	    # 	print(product_text)



	    	








        
