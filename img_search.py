from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib

def search(search_input):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get('https://www.google.com/imghp?hl=en')

    searchbar = browser.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    searchbar.send_keys(str(search_input))
    searchbar.send_keys(Keys.RETURN)

    image = browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').get_attribute('src')
    urllib.request.urlretrieve(image, 'SEARCH_IMG.png')
    browser.quit()