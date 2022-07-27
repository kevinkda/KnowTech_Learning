# !pip install kora - q
from kora.selenium import wd
# from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import csv
import time

all_list = []


class Amazon(object):
    def __init__(self):
        self.url = 'https://www.amazon.com/s?k=%E7%A7%AF%E6%9C%A8&ref=nb_sb_noss'
        # self.browser = webdriver.Chrome('sample_data/chromedriver')
        # self.browser = webdriver.Chrome(r'/content/sample_data/chromedriver')
        self.browser = wd

    def __del__(self):
        self.browser.close()

    def get_html(self):
        time.sleep(3)
        text = self.browser.page_source
        html = etree.HTML(text)

        productTitle = html.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
        urls = html.xpath('//a[@class="a-link-normal s-no-outline"]/@href')
        title = html.xpath('//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()')
        pinfen = html.xpath('//span[@class="a-icon-alt"]/text()')
        rating_value = html.xpath('//span[@class="a-size-base"]/text()')
        prcie = html.xpath('//span[@class="a-offscreen"]/text()')
        for i in range(0, len(urls)):
            try:
                print(title[i], pinfen[i], rating_value[i], urls[i], prcie[i])
                list = [title[i], pinfen[i], rating_value[i], urls[i], prcie[i]]
                all_list.append(list)
            except Exception as e:
                pass

    def main(self):
        time.sleep(2)
        self.browser.get(self.url)
        result = self.get_html()
        print(result)


if __name__ == '__main__':
    amazon_spider = Amazon()
    amazon_spider.main()
