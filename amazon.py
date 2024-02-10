from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup



def Harvey(url):

	###gives exe path to driver
    service = Service(executable_path='/home/gunjan/Downloads/chromedriver')
    driver = webdriver.Chrome(service= service)

    ## Open the URL in the browser
    driver.get(url)
    ##Maximizing the exe driver
    driver.maximize_window()

    ## Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    title = driver.find_element("xpath", '//span[@id="productTitle"]').text
    product_description = soup.find('div', {'id': 'productDescription'}).text.strip() if soup.find('div', {'id': 'productDescription'}) else None
    images = driver.find_elements("xpath",'//div[@id="altImages"]//img[@src]')
    image_sources = [img.get_attribute('src') for img in images]
    price = soup.find('div', {'id': 'corePrice_feature_div'}).find('span', {'data-a-color': 'price'}).find('span', {'class': 'a-offscreen'}).text
    selling_price = price
    discounted_price=""

    print(title)
    print(product_description)
    print(image_sources)
    print(price)
    print(selling_price)


    #closing driver
    driver.close()

url = 'https://www.amazon.in/Dettol-Antiseptic-Liquid-1-L/dp/B07B11V59H/ref=sr_1_1_sspa?crid=34VGD4ISNYXAF&keywords=dettol&qid=1704262549&sprefix=dettol%2Caps%2C235&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'


Harvey(url)
