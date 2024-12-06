# 셀레늄 기본세팅
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# 셀레늄에서 사용할 메서드들 임포트
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()

# options.add_argument("incognito")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

"""깃허브 크롤링
driver.get("https://github.com/")
sign_in = driver.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/header/div/div[2]/div/div/div/a')
sign_in.click()

github_id = driver.find_element(By.XPATH, '//*[@id="login_field"]')
github_id.send_keys("jerrygo009@gmail.com")

github_pw = driver.find_element(By.XPATH, '//*[@id="password"]')
github_pw.send_keys("dallae001")
time.sleep(1)
sign_in_green = driver.find_element(
    By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
sign_in_green.click()
time.sleep(1)
profile_icon = driver.find_element(
    By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[3]/deferred-side-panel/include-fragment/react-partial-anchor/button/span/span/img')
profile_icon.click()
time.sleep(1)

user_nickname = driver.find_element(
    By.XPATH, '//*[@id=":r6:"]/div/div/div/div[1]/div')
user = user_nickname.get_attribute("title")
print("nickname :",user)
user_name = driver.find_element(
    By.XPATH, '//*[@id=":r6:"]/div/div/div/div[2]/div')
user = user_name.get_attribute("title")
print("name :", user)

"""
''' 노트북실습
driver.get("https://www.danawa.com/")


search = driver.find_element(By.XPATH, '//*[@id="AKCSearch"]')
search.send_keys("노트북")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(1)


price = driver.find_element(
    By.XPATH, '//*[@id="priceRangeMinPriceOnSimpleSearchOption"]')

price.send_keys("500000")


ok = driver.find_element(By.XPATH, '//*[@id="priceRangeSearchButtonSimple"]')
ok.click()
time.sleep(3)

products = driver.find_element(By.XPATH, '//*[@id="productItem44762393"]/div')


name = products.find_element(
    By.XPATH, '//*[@id="productItem44762393"]/div/div[2]/p/a').text
price = products.find_element(
    By.XPATH, '//*[@id="productInfoDetail_44762393"]/p[2]/a').text
print(f"제품 이름: {name}, 가격: {price}")


input("대기")
'''
driver.get("https://www.agoda.com/ko-kr/?ds=ZkwJDIkPkJTItAVo")

time.sleep(5)
search = driver.find_element(By.XPATH, '//*[@id="textInput"]')
search.send_keys("삿포로")
time.sleep(5)
sapporo = driver.find_element(By.XPATH, '//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[6]/ul/div/ul/li[1]')

time.sleep(3)
sapporo.click()

time.sleep(5)
# day_start = driver.find_element(By.XPATH, '//*[@id="check-in-box"]/div')
# day_start.click()
day__1206 = driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[2]/div[5]/div')
day__1206.click()
day__1208 = driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[2]/div[7]/div')
day__1208.click()

search_botton = driver.find_element(By.XPATH, '//*[@id="Tabs-Container"]/button')
time.sleep(1)
search_botton.click()

time.sleep(5)
# hotel = driver.find_element(
#     By.XPATH, '//*[@id="contentContainer"]/div[4]/ol[1]/li[1]/div/a/div/div')


hotel_name = driver.find_element(By.XPATH, '//*[@id="contentContainer"]/div[4]/ol[2]/li[2]/div/div/div/div/div/div[2]/div/header/div[1]/a/span').text
hotel_cost = driver.find_element(By.XPATH, '//*[@id="contentContainer"]/div[4]/ol[2]/li[2]/div/div/div/div/div/div[3]/div/div[2]/aside[2]/ul/li[2]/div/div/div/span[3]').text
print(f"호텔 : {hotel_name}")
print(f"호텔 가격 : {hotel_cost}원")


input("대기")
