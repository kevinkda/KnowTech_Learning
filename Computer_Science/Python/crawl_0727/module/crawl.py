!pip install parsel
import requests
from parsel import Selector
from urllib.parse import urljoin

import json


def crawl(asin_no: str) -> dict:
    base_url: str = 'https://www.amazon.cn/dp/' + asin_no + '/ref=z_cn'
    headers: dict = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    resp = requests.get(base_url, headers=headers)
    # print(str(resp))

    content = resp.content.decode('utf-8')
    # print(str(content))

    select = Selector(text=content)

    # print(str(select))

    productTitle = select.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
    # ags_shipping_import_fee = select.xpath('//*[@id="ags_shipping_import_fee"]/text()').extract_first()
    print("productTitle: " + productTitle)
    # print("ags_shipping_import_fee: "+ags_shipping_import_fee)

    # merchant_id = select.xpath('//*[@id="merchantID"]/text()').extract_first().strip()
    merchant_id = select.css('#merchantID').re_first(
        '<input type="hidden" id="merchantID" name="merchantID" value="(.*?)">')
    # merchant_id = selector.css('.item-0').re_first('<span class="bold">(.*?)</span>')
    print("merchant_id: " + merchant_id)

    # asin_info = {
    #     "productTitle": select.xpath("/text()"),
    #     "ags_shipping_import_fee": select.xpath("/text()")
    # }

    asin_info = {
        "productTitle": select.xpath('//*[@id="productTitle"]/text()').extract_first().strip(),
        # "ags_shipping_import_fee": select.xpath('//*[@id="ags_shipping_import_fee"]/text()').extract_first().strip()
        "ags_shipping_import_fee": ags_shipping_import_fee(asin_no, merchant_id)
    }

    return asin_info


def ags_shipping_import_fee(asin_no: str, merchant_id: str) -> float:
    # base_url: str = 'https://data.amazon.cn/api/marketplaces/AAHKV2X7AFYLW/products/' + asin_no + '?merchantId=' + merchant_id
    base_url: str = 'https://data.amazon.cn/api/marketplaces/AAHKV2X7AFYLW/products/' + asin_no + '?merchantId=A3CQWPW49OI3BQ'
    headers: dict = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Accept": "application/vnd.com.amazon.api+json; type=\"product/v2\"; expand=\"buyingOptions[].importDetails(product.import-details/v1),buyingOptions[].globalStore(product.global-store/v1)\"",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN",
        "X-API-CSRF-TOKEN": "1@g2jHUE/lKD6Cbh/0mPy1WnhnUN+Xp6X/LKZ71DbkouvRAAAAAQAAAABi4OADcmF3AAAAABVX8CwXqz42z+J7i/ABqA==@NLD_5740BY",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }

    resp = requests.get(base_url, headers=headers)
    content = resp.content.decode('utf-8')

    print("content:"+content)

    # resp_json = json.loads(content)
    # ags_shipping_import_fee = resp_json["entity"]['buyingOptions'](0)['importDetails']['entity']['fee']['amount']

    return float(ags_shipping_import_fee)


if __name__ == '__main__':
    product_info: dict = crawl(asin_no='B0050N5DPY')
    print(product_info)
