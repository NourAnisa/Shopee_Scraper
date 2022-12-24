from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import random
import requests
from datetime import datetime
import sys
import json

url = 'https://shopee.co.id/search?keyword=celana%20jeans%20stretch%20pria&page=0'

# options = Options()
browser = webdriver.Chrome(
    "chromedriver.exe")
#myclient = pymongo.MongoClient ("mongodb://localhost:27017/")
#db = myclient["admin"]
#collection = db["marketplace"]

batch_number = "Batch-" + datetime.today().strftime('%Y%m%d') + "-" + \
    str(random.randint(1, 999999999999))


def searchComment():
    time.sleep(5)
    browser.execute_script('window.scrollTo(0, 4500);')
    time.sleep(5)
    browser.execute_script('window.scrollTo(0, 5500);')

    soup = BeautifulSoup(html, 'html.parser')
    table_temp = soup.find_all('div', {"class": "shopee-product-rating"})
    # data = []
    for index, value in enumerate(table_temp):
        div_akun = value.find("a", class_="shopee-product-rating__author-name")
        nama_akun = ''
        rating_komentator = 0
        url_akun_komentator = ''
        if div_akun is not None:
            nama_akun = div_akun.text

            div_anchor_comentator = div_akun['href']
            url_detail = 'https://shopee.co.id' + div_anchor_comentator
            browser.get(url_detail)
            time.sleep(5)
            browser.execute_script('window.scrollTo(0, 1500);')
            time.sleep(5)
            html2 = browser.page_source
            soup_2 = BeautifulSoup(html2, 'html.parser')

            label_rating_komentator = soup_2.find(
                "div", class_="section-seller-overview__item section-seller-overview__item--clickable").find(class_="section-seller-overview__item-text-value")
            # label_rating_komentator = soup_2.find("div", string = "penilaian)")
            # print(label_dimensi)
            # exit()
            if label_rating_komentator is not None:
                url_akun_komentator = url_detail
                rating_komentator = label_rating_komentator.text

        rating = value.find_all("svg", {"class": "icon-rating-solid--active"})
        div_komentar = value.find('div', class_="_3NrdYc")
        komentar = ''
        if div_komentar is not None:
            komentar = div_komentar.text

        indikasi_negatif = 0
        kata_indikasi = ''
        if "tapi" in komentar or "tp" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'tapi'

        if "agak" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'agak'

        if "teliti" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'teliti'

        if " lama " in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'lama'

        if "gpp" in komentar or "gak papa" in komentar or "gk papa" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'gpp'

        if "beda" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'beda'

        if "sebenarnya" in komentar or "sebenernya" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'sebenarnya'

        if "cuma" in komentar or "cm" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'cuma'

        if "meski" in komentar or "meskipun" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'meski'

        if "walau" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'walau'

        if "kecewa" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'kecewa'

        if "ternyata" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'ternyata'

        if "maaf" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'maaf'

        if "tidak sesuai" in komentar or "gak sesuai" in komentar or "gk sesuai" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'tidak sesuai'

        # if "kegedean" in komentar:
        #     indikasi_negatif = 1
        #     kata_indikasi = 'kegedean'

        # if "kekecilan" in komentar:
        #     indikasi_negatif = 1
        #     kata_indikasi = 'kekecilan'

        # if "terlalu kecil" in komentar or "terlalu besar" in komentar:
        #     indikasi_negatif = 1
        #     kata_indikasi = 'terlalu'

        if "sayang" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'sayang'

        if "kurang" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'kurang'

        if "susah" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'susah'

        if "minus" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'minus'

        if "datengnya" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'yang datang'

        if "yang dateng" in komentar or "yg dateng" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'yang datang'

        if "yang datang" in komentar or "yg datang" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'yang datang'

        if "tidak sama" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'tidak sama'

        if "yang salah" in komentar or "yg salah" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'salah'

        if "seharusnya" in komentar or "harusnya" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'seharusnya'

        if "kirain" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'kirain'

        if "sobek" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'sobek'

        if "rusak" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'rusak'

        if "sedikit" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'sedikit'

        if "padahal" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'padahal'

        if "lumayan" in komentar:
            indikasi_negatif = 1
            kata_indikasi = 'lumayan'

        data_produk = dict()
        data_produk["nama_akun"] = nama_akun
        data_produk["komentar"] = komentar
        data_produk["url_akun_komentator"] = url_akun_komentator
        data_produk["rating_komentator"] = rating_komentator
        data_produk["rating"] = len(rating)
        data_produk["indikasi_negatif"] = indikasi_negatif
        data_produk["kata_indikasi"] = kata_indikasi
        # data_produk["terjual"] = sold

        if len(rating) > 1:
            with open("data_comment.json", "a") as data:
                data.write(json.dumps(data_produk) + ', ')
                data.close()

    # return data_produk


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
    div_product_name = soup.find("div", class_="KVhuC3")
    if div_product_name is not None:
        product_name = div_product_name.find_next_sibling("span")
        return product_name.text

    # div_title = soup.find("span", class_ = "$0")
    # if div_title is not None:
    #   product_name = div_title.text
    #   return product_name

    return ''


def getMerek(soup):
    link_merek = soup.find("a", class_="_3Qy6bH")
    if link_merek is not None:
        merek = link_merek.text
        return merek

    # label_merek = soup.find("label", string = "Merek")
    # if label_merek is not None:
    #   merek = label_merek.find_next_sibling("div").text
    #   return merek

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
    with open("data_marketplace.json", "a") as data:
        data.write(json.dumps(obj) + ', ')
        data.close()

    return obj


all_data = []
counter = 0
while (counter <= 5):
    if counter > 4:
        counter = 1
    counter += 1
    # base_url = 'https://shopee.co.id/search?keyword=hijab&page=' + str(counter)
    # base_url = 'https://shopee.co.id/search?keyword=jaket%20pria&page=' + str(counter)
    # base_url = 'https://shopee.co.id/search?keyword=gamis&page='+ str(counter)
    base_url = 'https://shopee.co.id/search?keyword=sepatu%20pria&page=' + \
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
        label_shop_name = soup.find("div", class_="_1wVLAc")
        if label_shop_name is not None:
            shop_name = label_shop_name.text

        label_product_origin = soup.find("label", string="Dikirim Dari")
        product_origin = ''
        if label_product_origin is not None:
            product_origin = label_product_origin.find_next_sibling("div").text

        # sold = soup.find("div", class_ = "_3b2Btx").text
        div_rating = soup.find("div", class_="URjL1D")
        rating = ''
        if div_rating is not None:
            rating = div_rating.text

        div_harga = soup.find("div", class_="pmmxKx")
        harga = ''
        if div_harga is not None:
            harga = div_harga.text

        div_jumlah_ulasan = soup.find("div", class_="_1GknPu")
        jumlah_ulasan = ''
        # if jumlah_ulasan is not None:
        # jumlah_ulasan = div_jumlah_ulasan.find_next_sibling('div').text

        data_produk = dict()
        data_produk["marketplace_name"] = 'shopee'
        # data_produk["link"] = url_detail
        data_produk["nama_produk"] = product_name
        data_produk["harga"] = harga
        data_produk["shop_name"] = shop_name
        data_produk["lokasi_penjual"] = product_origin
        # data_produk["terjual"] = sold
        data_produk["rating"] = rating
        data_produk["jumlah_ulasan"] = jumlah_ulasan
        # searchComment()

        with open("data_marketplace_ulasan_shopee.json", "a") as data:
            data.write(json.dumps(data_produk) + ', ')
            data.close()
        # print(data_produk)
        # sys.exit()
        # if temp:
        #         all_data.append(temp)

# print(all_data)
# if all_data:
#   x = collect÷on.insert_many(all_data)
