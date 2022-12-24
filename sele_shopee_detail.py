from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime
import sys
import json

url = 'https://shopee.co.id/search?keyword=celana%20jeans%20stretch%20pria&page=0'

# options = Options()
browser = webdriver.Chrome("chromedriver.exe")
#myclient = pymongo.MongoClient ("mongodb://localhost:27017/")
#db = myclient["admin"]
#collection = db["marketplace"]

batch_number = "Batch-" + datetime.today().strftime('%Y%m%d') + "-" + \
    str(random.randint(1, 999999999999))


def search(base_url):
    browser.get(base_url)
    time.sleep(5)
    browser.execute_script('window.scrollTo(0, 1500);')
    time.sleep(5)
    browser.execute_script('window.scrollTo(0, 2500);')
    time.sleep(5)
    html = browser.page_source
    # browser.close()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('div', {"class": "shopee-search-item-result__item"})
    data = []
    for x, div in enumerate(table):
        tag_link = div.find("a")
        if tag_link is not None:
            data.append(tag_link.get('href'))

    return data


def getProductName(soup):
    div_product_name = soup.find("div", class_="_1x8-jJ")
    if div_product_name is not None:
        product_name = div_product_name.find_next_sibling("span")
        return product_name.text

    # div_title = soup.find("span", class_ = "$0")
    # if div_title is not None:
    # 	product_name = div_title.text
    # 	return product_name

    return ''


def getMerek(soup):
    link_merek = soup.find("a", class_="_3Qy6bH")
    if link_merek is not None:
        merek = link_merek.text
        return merek

    # label_merek = soup.find("label", string = "Merek")
    # if label_merek is not None:
    # 	merek = label_merek.find_next_sibling("div").text
    # 	return merek

    return ''


def product_detail(url_suffix):
    url_detail = 'https://shopee.co.id' + url_suffix
    browser.get(url_detail)
    time.sleep(5)
    browser.execute_script('window.scrollTo(0, 1500);')
    time.sleep(5)
    browser.execute_script('window.scrollTo(0, 2500);')
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    data = []

    # PRODUCT NAME
    product_name = getProductName(soup)
    shop_name = ''
    label_shop_name = soup.find("div", class_="_3uf2ae")
    if label_shop_name is not None:
        shop_name = label_shop_name.text

    string_price = soup.find("div", class_="Ybrg9j").text
    remove_dot = string_price.replace(".", "")
    price = remove_dot.replace("Rp", "")

    label_rating = soup.find("div", class_="_3Oj5_n")
    rating = ''
    if label_rating is not None:
        rating = label_rating.text
    merek = getMerek(soup)

    label_bahan = soup.find("label", string="Bahan")
    bahan = ''
    if label_bahan is not None:
        bahan = label_bahan.find_next_sibling("div").text

    label_style = soup.find("label", string="Style")
    style = ''
    if label_style is not None:
        style = label_style.find_next_sibling("div").text

    label_dimensi = soup.find("label", string="Dimensi")
    dimensi = ''
    if label_dimensi is not None:
        dimensi = label_dimensi.find_next_sibling("div").text

    label_location = soup.find("label", string="Dikirim Dari")
    location = ''
    if label_location is not None:
        location = label_location.find_next_sibling("div").text

    label_product_origin = soup.find("label", string="Asal Produk")
    product_origin = ''
    if label_product_origin is not None:
        product_origin = label_product_origin.find_next_sibling("div").text

    label_stock = soup.find("label", string="Stok")
    stock = ''
    if label_stock is not None:
        stock = label_stock.find_next_sibling("div").text

    is_insert = False
    include_category = ["Fashion Muslim", "Pakaian Wanita"]
    product_category = []
    for temp_category in soup.find_all("a", class_="JFOy4z"):
        if temp_category.text in include_category:
            is_insert = True
        product_category.append(temp_category.text)

    if not is_insert:
        return False

    label_description = soup.find("div", class_="_2u0jt9")
    description = ''
    if label_description is not None:
        description = label_description.text

    sold = soup.find("div", class_="_22sp0A").text

    label_review = soup.find("div", string="penilaian")
    total_review = ''
    if label_review is not None:
        label_total_review = label_review.find_previous_sibling("div")
        if label_total_review is not None:
            total_review = label_total_review.text

    customer_review = []
    for temp_review in soup.find_all("div", class_="shopee-product-rating__content"):
        customer_review.append(temp_review.text)

    product_color = []
    for temp_color in soup.find_all("button", class_="product-variation"):
        product_color.append(temp_color.text)

    data_produk = dict()
    data_produk["marketplace_name"] = 'shopee'
    data_produk["link"] = url_detail
    data_produk["shop_name"] = shop_name
    return shop_name
    obj = {
        'marketplace_name': 'shopee',
        'link': url_detail,
        'shop_name': shop_name,
        # 'shop_category': '',
        # 'location': location,
        # 'product_name': product_name,
        # 'product_category': product_category,
        # 'price': price,
        # 'rating': rating,
        # 'total_review':  total_review,
        # 'sold': sold,
        # 'merek': merek,
        # 'bahan': bahan,
        # 'dimensi': dimensi,
        # 'style': style,
        # 'product_origin': product_origin,
        # 'stock': stock,
        # 'product_color': product_color,
        # 'customer_review': customer_review,
        # 'description': description,
        # 'total_views': '',
        # 'insert_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        # 'date': datetime.now().strftime('%Y-%m-%d'),
    }
    with open("data_marketplace_shopee_detail.json", "a") as data:
        data.write(json.dumps(obj) + ', ')
        data.close()

    return obj


all_data = []
counter = 0
while (counter <= 5):
    if counter > 4:
        counter = 1
    counter += 1
    base_url = 'https://shopee.co.id/search?keyword=celana%20jeans%20stretch%20pria&page=' + \
        str(counter)
    product_urls = search(base_url)
    for index, product_url in enumerate(product_urls):
        url_detail = 'https://shopee.co.id' + product_url
        browser.get(url_detail)
        time.sleep(5)
        browser.execute_script('window.scrollTo(0, 1500);')
        time.sleep(5)
        browser.execute_script('window.scrollTo(0, 2500);')
        time.sleep(5)
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        product_name = getProductName(soup)
        shop_name = ''
        label_shop_name = soup.find("div", class_="_3uf2ae")
        if label_shop_name is not None:
            shop_name = label_shop_name.text

        label_product_origin = soup.find("label", string="Dikirim Dari")
        product_origin = ''
        if label_product_origin is not None:
            product_origin = label_product_origin.find_next_sibling("div").text

        sold = soup.find("div", class_="aca9MM").text

        data_produk = dict()
        data_produk["marketplace_name"] = 'shopee'
        data_produk["link"] = url_detail
        data_produk["nama_produk"] = product_name
        data_produk["shop_name"] = shop_name
        data_produk["lokasi_penjual"] = product_origin
        data_produk["terjual"] = sold

        with open("data_marketplace_shopee_detail.json", "a") as data:
            data.write(json.dumps(data_produk) + ', ')
            data.close()
        # print(data_produk)
        # sys.exit()
        # if temp:
        #         all_data.append(temp)

# print(all_data)
# if all_data:
# 	x = collect÷on.insert_many(all_data)
