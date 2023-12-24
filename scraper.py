from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import json


def bukabrowser(query):
    link = "https://www.tokopedia.com/search?st=&q="+query
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1'
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-javascript")
    options.add_argument("--headless")
    options.add_argument(f'user-agent={user_agent}')
    
    # servis = Service("chromedriver.exe")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get(link)
    time.sleep(5)
    # driver.get_screenshot_as_file("tes.png")
    content = driver.page_source
    driver.quit()
    data = BeautifulSoup(content, 'html.parser')
    base_url = "https://www.tokopedia.com"
    list_cari = []
    for area in data.find_all('div', class_="pcv3__container css-1izdl9e"):
        nama = area.find('div', class_="prd_link-product-name css-3um8ox").get_text()
        urlitem = area.find('a', class_="pcv3__info-content css-gwkf0u")['href']
        if "https://ta.tokopedia.com" not in urlitem:
            urlitem=base_url+urlitem
        harga = area.find('div', class_="prd_link-product-price css-h66vau").get_text()
        toko = str(area.find('span', class_="prd_link-shop-name css-1kdc32b flip")).replace('<span class="prd_link-shop-name css-1kdc32b flip" data-testid="linkShopName">', '').replace('</span>', '')
        value = {
            'nama':nama,
            'harga':harga,
            'toko':toko,
            'link':urlitem
        }
        list_cari.append(value)
        # print(json.dumps(value))

    value={
        'data':list_cari
    }

    hasil = json.dumps(value)
    return hasil
    

        
    


