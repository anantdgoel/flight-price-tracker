import os
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def united():
    chromedriver = "/Users/anantgoel/Downloads/chromedriver"
    os.environ["webdrive.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.united.com/ual/en/us/flight-search/book-a-flight/results/rev?f=CHI&t=DLH&d=2017-03-10&tt=1&sc=7&px=1&taxng=1&idx=1")
    time.sleep(5)
    page_source = driver.page_source.encode('utf-8')
    driver.close()
    parser = BeautifulSoup(page_source, 'html.parser')
    elem = parser.find(id="sr_product_ECONOMY_69-5030")
    price = elem.div.div.text
    price = str(price)
    int_price = re.findall('\d+', price)
    price = int(int_price[0])
    print(price) #just a debug statement to check my script's logic
    if price < 161 :
        print "Found cheap ticket"
    else:
        print "Price is still too high"

if __name__ == '__main__':
    united()
