import time
from bs4 import BeautifulSoup
import requests
import pprint

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.77",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get('https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"usersSearchTerm"%3A"San%20Francisco%2C%20CA"%2C"mapBounds"%3A%7B"west"%3A-122.44334881417362%2C"east"%3A-122.18070690743534%2C"south"%3A37.72974613095393%2C"north"%3A37.890320889320165%7D%2C"mapZoom"%3A12%2C"regionSelection"%3A%5B%7B"regionId"%3A20330%2C"regionType"%3A6%7D%5D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"price"%3A%7B"min"%3A0%2C"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"min"%3A0%2C"max"%3A3000%7D%2C"ah"%3A%7B"value"%3Atrue%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%7D', headers=headers)

content = response.text

soup = BeautifulSoup(content,"lxml")
v = soup.find(name="ul", class_="photo-cards").find_all(name="li")
# pprint.pprint(v)
for x in v:
    b = x.get_text()
    print(b)
