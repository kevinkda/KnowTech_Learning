!pip install selenium urllib3
from selenium import webdriver
import time
from lxml import etree
import pandas as pd
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait


def spider_data(num, aa):
    # 让浏览器 不加载图片、css样式
    chrome_options = Options()
    prefs = {
        'profile.managed_default_content_settings.images': 2,
        'permissions.default.stylesheet': 2
    }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--headless')

    desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

    # driver = webdriver.Chrome(r'C:\Lee\pycharm\selenium_chorme插件\chromedriver.exe', chrome_options=chrome_options)

    # driver = webdriver.Chrome(r'C:\Lee\pycharm\selenium_chorme插件\chromedriver.exe')
    url = 'https://www.amazon.com/dp/' + num

    asin_s = []
    stock_s = []  # 库存数据
    stock_mark = []  # 是否限购标记

    asin_s.append(num)

    # 隐式等待
    # driver.implicitly_wait(5)
    driver.get(url)
    try:
        element1 = WebDriverWait(driver, 4, 0.5).until(
            expected_conditions.presence_of_element_located((By.ID, 'add-to-cart-button')))
        # # 1.获取页面对象的 加入购物车 按钮，并点击
        # # driver.find_element_by_id("add-to-cart-button").click()
        element1.click()

        # 2.找到亚马逊右上角的 含有商品的购物车图标，并点击
        driver.find_element_by_id('nav-cart-count').click()

        # 3.找到输入框的定位元素，并点击
        driver.find_element_by_id('a-autoid-0-announce').click()

        # 4.选择下拉框最底部的 最大值，并点击
        driver.find_element_by_id('quantity_10').click()

        try:
            # 5.定位输入框，并输入最大值999
            driver.find_element_by_name('quantityBox').send_keys('999')
            print('已输入数字')
            time.sleep(1)
            # 6.点击 确定按钮
            driver.find_element_by_id('a-autoid-1-announce').click()
            time.sleep(2)
            html = driver.page_source
            # print(html)
            a = etree.HTML(html)

            # 不同页面的 目标数据 位置不一样
            num1 = a.xpath('//div[@class="a-popover-content"]/text()')
            num2 = a.xpath('//div[@class="a-alert-content"]/span[@class="a-size-base"]/text()')
            result = num1 or num2 if num1 or num2 else ' '
            print(result)
            if '只有' in result[0]:
                stock_s.append(result[0].replace('\n此商品在您选择的卖家处只有', '').replace('件。到', ''))
                stock_mark.append('False')
            elif '限制' in result[0]:
                stock_s.append(result[0].replace('\n此卖家对该商品的数量限制为每位客户', '').replace('件。到', ''))
                stock_mark.append('True')
            else:
                stock_s.append(' ')
                stock_mark.append('Not updated')

            # 保存数据
            data = {'target_asin': asin_s,
                    'stock_num': stock_s,
                    'stock_mark': stock_mark}
            df = pd.DataFrame(data, columns=['target_asin', 'stock_num', 'stock_mark'])
            df.to_csv('stock_data.csv', mode='a', index=False, encoding='utf_8_sig')
            print('爬取成功：', str(aa))

            # 关闭页面
            driver.quit()

        except Exception as error:
            print('fail：', error)
            # 关闭页面
            driver.quit()
    except:
        print(num, '缺货中')
        stock_s.append(0)
        stock_mark.append('-')

        # 保存数据
        data = {'target_asin': asin_s,
                'stock_num': stock_s,
                'stock_mark': stock_mark}
        df = pd.DataFrame(data, columns=['target_asin', 'stock_num', 'stock_mark'])
        df.to_csv('stock_data.csv', mode='a', index=False, encoding='utf_8_sig')

        # 关闭页面
        driver.quit()


if __name__ == '__main__':
    # 这里需要用excel记录一列需要爬取的asin数据，列字段为asin
    # df = pd.read_excel(r'C:\Users\sparkx\Desktop\asin_data.xlsx')
    aa = 0
    # for num in df['asin']:
    #     aa += 1
    #     spider_data(num, aa)
        # time.sleep(1)

    num='B0050N5DPY'
    spider_data(num, aa)
