from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import json

url = 'https://www.bukalapak.com/p/kamera/kamera-analog/42j63i9-jual-ilford-delta-400-film-bulk-digulung-menjadi-27-exposure-fresh?from=list-product&keyword=&funnel=omnisearch&product_owner=normal_seller&pos=0&cf=1&ssa=1&sort_origin=last_relist_at%3Adesc&search_sort_default=false&promoted=1'
url = 'https://www.bukalapak.com/p/fashion-wanita/bahan-kain/3zyk0mz-jual-kain-bahan-kaos-katun-kiloan-cotton-combed-24s-ultima-premium-warna-tua-paket-1-kg-dan-rib?from=list-'
# options = Options()
# options.add_argument("--headless")
obj = {
		'marketplace_name': 'shopee 1',
		'link' : 'url_detail',
		'shop_name': 'a',
		'shop_category': 'b',
		'location': 'c',
	}

with open("data_marketplace.txt", "a") as data:
	data.write(json.dumps(obj)+',')
	data.close()
# remove_dot = string_price.replace(".", "")
# price = remove_dot.replace("Rp", "")
# total_review = span_total_views.find_previous_sibling("b").text

# print(shop_category)
# data = []
# table = soup.find_all('div', {"class":"shopee-search-item-result__item"})
# for x, div in enumerate(table):
# 	title = div.find("div", class_ = "_1NoI8_")
# 	price = div.find("span", class_ = "_341bF0")
# 	location = div.find("div", class_ = "_3amru2")
# 	sold = div.find("div", class_ = "_18SLBt")
	
# 	fix_title = ''
# 	if title is not None:
# 		fix_title = title.text

# 	fix_price = ''
# 	if price is not None:
# 		fix_price = price.text

# 	fix_location = ''
# 	if location is not None:
# 		fix_location = location.text

# 	fix_sold = ''
# 	if sold is not None:
# 		fix_sold = sold.text

# 	obj = {
# 		"name" : fix_title,
# 		"price" : fix_price,
# 		"location" : fix_location,
# 		"sold" : fix_sold,
# 	}
# 	data.append(obj)

# print(data)