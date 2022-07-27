from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re

driverPath = r"G:\code\python\TikTokSelenium\driver\chromedriver.exe"


def getData():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument('headless')
    service = Service(executable_path=driverPath)
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.amazon.cn/dp/B007II23XO/ref=z_cn?th=1&psc=1%27')
    delivery = driver.find_element_by_id('delivery-block-ags-dcp-container_0').text
    taxation = driver.find_element_by_id('ags_shipping_import_fee').text
    print(delivery, taxation)


if __name__ == '__main__':
    getData()
