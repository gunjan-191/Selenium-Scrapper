from selenium import webdriver


def Harvey(url):
	
	driver = webdriver.Chrome(executable_path='E://gunjan//chromedriver.exe')
	driver.get(url)

	driver.maximize_window()

	title = driver.find_element_by_xpath('//*[@id="overview"]/div[1]/h1/span[1]').text
	print(title)


	#click the review button
	driver.find_element_by_xpath('//*[@id="tab-product-reviews"]').click()


	driver.implicitly_wait(10) # seconds

# 	#click Show all
# 	driver.find_element_by_xpath('//*[@id="BVRRContainer"]/div/div/div/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div/p/a').click()

	review =driver.find_element_by_xpath('//*[@id="BVRRContainer"]/div/div/div/div/ol/li[1]/div[2]/div[1]/div/div[1]/div/div[2]/h3').text
	print(review)

	driver.close()

url = 'https://www.harveynorman.com.au/hp-14-inch-celeron-n4020-4gb-64gb-emmc-laptop.html'


Harvey(url)
