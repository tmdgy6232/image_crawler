import ssl
from selenium import webdriver
import time
from urllib.request import urlopen
from urllib.parse import quote_plus

# 셀레니움 설정
driver = webdriver.Chrome('/Users/imseunghyo/dev/chromedriver')

# CERTIFICATE_VERIFY_FAILED 에러 수정
context = ssl._create_unverified_context()

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
searchWord = input('검색어 입력 : ')
image_nums = int(input('크롤링 할 갯수 입력 : '))

request_url = baseUrl + quote_plus(searchWord) # 한글검색 자동변환

driver.get(request_url)

#
time.sleep(3)

img = driver.find_elements_by_css_selector('.sc_new ._image')

num = 1
for i in img:
    print(num)
    imgUrl = i.get_attribute('src')
    with urlopen(imgUrl, context=context) as f:
        with open('./images/img' + str(num)+'.jpg', 'wb') as h: # write binary
            img = f.read()
            h.write(img)
    num += 1
    if num > image_nums:
        break

print('Image Crawling is done')