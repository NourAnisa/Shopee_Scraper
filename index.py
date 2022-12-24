from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time
import random
import requests
from datetime import datetime
import sys
import json

browser = webdriver.Chrome("chromedriver.exe")

url_detail = 'https://shopee.co.id/shop/22791283'
browser.get(url_detail)
time.sleep(5)
browser.execute_script('window.scrollTo(0, 1500);')
time.sleep(5)
html = browser.page_source
soup_2 = BeautifulSoup(html, 'html.parser')

label_rating_komentator = soup_2.find("div", class_="section-seller-overview__item section-seller-overview__item--clickable")[
    1].find(class_="section-seller-overview__item-text-value")
product_name = label_rating_komentator.find_next_sibling("div")
print(label_rating_komentator)
exit()
