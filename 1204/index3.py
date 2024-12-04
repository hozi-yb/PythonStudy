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
sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/header/div/div[2]/div/div/div/a')
sign_in.click()

github_id = driver.find_element(By.XPATH, '//*[@id="login_field"]')
github_id.send_keys("jerrygo009@gmail.com")

github_pw = driver.find_element(By.XPATH, '//*[@id="password"]')
github_pw.send_keys("dallae001")
time.sleep(1)
sign_in_green = driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
sign_in_green.click()
time.sleep(1)
profile_icon = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[3]/deferred-side-panel/include-fragment/react-partial-anchor/button/span/span/img')
profile_icon.click()
time.sleep(1)

user_nickname = driver.find_element(By.XPATH, '//*[@id=":r6:"]/div/div/div/div[1]/div')
user = user_nickname.get_attribute("title")
print("nickname :",user)
user_name = driver.find_element(By.XPATH, '//*[@id=":r6:"]/div/div/div/div[2]/div')
user = user_name.get_attribute("title")
print("name :", user)

"""
driver.get("https://www.danawa.com/")

search = driver.find_element(By.XPATH, '//*[@id="AKCSearch"]')
search.send_keys("노트북")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(1)
price = driver.find_element(By.XPATH, '////*[@id="priceRangeMinPriceOnSimpleSearchOption"]')
price.send_keys("500000")

ok = driver.find_element(By.XPATH, '//*[@id="priceRangeSearchButtonSimple"]')
ok.click()
time.sleep(3)
products = driver.find_element(By.XPATH, '//*[@id="productItem44762393"]/div/div[2]/p/a')
name = products.text
print(name)


input("대기")