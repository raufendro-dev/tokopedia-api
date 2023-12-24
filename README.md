﻿# Tokopedia API

Tokopedia API adalah API unofficial untuk mendapatkan data item dari hasil pencarian barang berbentuk json. Tokopedia API merupakan web scraping dari halaman https://www.tokopedia.com/

### Run
Live link sample : http://103.193.178.139:2701/tokopedia?cari=macbook%20pro%20m1


## Cara penggunaan

### Install Library Python
Pertama install terlebih dahulu library python berikut
- Flask
- BeautifulSoup4
- Selenium
### Run WebServer
Jalankan file webAPI
- python3 webAPI.py
- buka pada browser, contoh : https://localhost:2701/tokopedia?cari=laptop

### Catatan
- Link pada browser bisa menggunakan ip atau domain anda
- Port bisa diubah di webAPI.py
- File logpengunjung.log adalah log dari pencarian user. Anda bisa menggunakannya jika dibutuhkan


