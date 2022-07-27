import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def crawl(asin_no: str) -> dict:
    base_url: str = 'https://www.amazon.cn/dp/' + asin_no + '/ref=z_cn'

    option = Options()
    option.add_experimental_option("detach", True)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--disable-blink-features=AutomationControlled')

    web = Chrome(options=option)
    web.get(base_url)

    time.sleep(2)

    # 获取商品名
    productTitle: str = web.find_element(By.XPATH, '//*[@id="productTitle"]').text
    time.sleep(2)

    web.find_element(By.XPATH, '//*[@id="native_dropdown_selected_size_name"]').click()
    time.sleep(1)

    web.find_element(By.XPATH, '//*[@id="native_size_name_11"]').click()
    time.sleep(3)

    ags_shipping_import_fee = web.find_element(By.XPATH, '//*[@id="ags_shipping_import_fee"]').text

    asin_info = {
        "productTitle": productTitle,
        "ags_shipping_import_fee": ags_shipping_import_fee
    }

    return asin_info


if __name__ == '__main__':
    product_info: dict = crawl(asin_no='B0050N5DPY')
    print(product_info)
