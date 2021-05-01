"""
button.btn-disabled
"""
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse

bestBuySelector = 'button.btn-disabled'
newEggSelector = 'i.fa-exclamation-triangle'

links = [
  'https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-latest-model-gold/6418599.p?skuId=6418599', 
  'https://www.newegg.com/asus-geforce-rtx-3090-rog-strix-rtx3090-o24g-white/p/N82E16814126482?Description=rtx%203090%20gpu&cm_re=rtx_3090%20gpu-_-14-126-482-_-Product', 
  'https://www.newegg.com/black-thermaltake-core-p3-tg-atx-open-frame-chassis/p/N82E16811133372?Item=N82E16811133372&Description=PPSSUPOKXQYLPC&cm_re=PPSSUPOKXQYLPC-_-11-133-372-_-Product&quicklink=true', 
  'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
  'https://www.bestbuy.com/site/hyperx-pudding-keycaps-pbt-upgrade-kit-white/6412547.p?skuId=6412547',
  'https://www.bestbuy.com/site/combo/ps5-consoles/8f146095-0a5f-4993-b123-711a1d34745b'
]

headers = {"User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

while True:
  for link in links:
    parsed_link = urlparse(link)
    company = parsed_link.netloc

    print("Company:", company)
    response = requests.get(link, headers = headers)
    page = response.content
    soup = BeautifulSoup(page, 'html.parser')
    
    if company == "www.bestbuy.com":
      selector = bestBuySelector
    elif company == "www.newegg.com":
      selector = newEggSelector
    soup.select(selector)
    result = soup.select(selector)

    # print("Selector:", result)

    if len(result) == 0: 
      print("Instock")
    else:
      print("out of stock")

    time.sleep(3)
