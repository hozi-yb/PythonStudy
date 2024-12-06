from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# 이 밑에 두개는 거의 같이 들어간다.
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

options = Options()

# options.add_argument("incognito")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#EC 메서드
# EC.title_is("문자열") # 현재 페이지 제목이 지정된 문자열과 일치할 때
# EC.title_contains("문자열") # 현재 페이지 제목에 문자열이 포함될 때
# EC.presence_of_all_elements_located((By.ID, "아이디값")) # By.ID는 예시,,, 아이디값의 DOM이 존재할 때 ( 화면표시 안되어도 됨. )
# EC.visibility_of_element_located((By.CSS_SELECTOR, "선택자값")) # CSS도 예시,,, DOM이 존재할 때 ( 화면에 표시 되어야됨. )
# EC.presence_of_all_elements_located((By.CSS_SELECTOR, "선택자")) # DOM에 모든요소가 존재할 때
# EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "선택자")) # DOM에 모든 요소가 존재할 떄..( find_element와 find_elements의 차이와 비슷)
# EC.element_to_be_clickable((By.CSS_SELECTOR, "선택자")) # 요소가 화면에 표시되고 클릭이 가능할 때.
# EC.element_to_be_selected((By.CSS_SELECTOR, "선택자")) # 요소가 선택된 상태가 될 때.

# 실습3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

driver.get("https://www.agoda.com/")
time.sleep(2)

search = driver.find_element(By.XPATH, '//*[@id="textInput"]')
click_search = search.click()
search_sapporo = search.send_keys("삿포로")

clickin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.Suggestion Suggestion__categoryName'))
)

clickin.click()

# time.sleep(2)
# sapporo = driver.find_element(By.XPATH, '//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[6]/div/div/ul/li[1]').click()

checkin_day = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[2]/div[5]'))
)
checkin_day.click()

checkout_day = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[2]/div[6]'))
)
checkout_day.click()

# time.sleep(1)
# search_botton = driver.find_element(By.XPATH, './/*[@id="Tabs-Container"]/button').click()

tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, './/*[@id="Tabs-Container"]/button'))
)
tab.click()

driver.switch_to.window(driver.window_handles[-1])
# print(driver.current_url)

time.sleep(10)
hotels = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.hotel-list-container h3'))
)

# hotels = driver.find_elements(By.CSS_SELECTOR, '.hotel-list-container h3')
price = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.hotel-list-container .PropertyCardPrice__Value'))
)
# price = driver.find_elements(By.CSS_SELECTOR, '.hotel-list-container .PropertyCardPrice__Value')

print(f"호텔명: {hotels[0].text}, 가격: {price[0].text}원")
'''

driver.get("https://www.agoda.com/ko-kr")

time.sleep(3)

search = driver.find_element(By.ID, 'textInput')
search.click()
search.send_keys("도쿄")
time.sleep(1)
search.send_keys(Keys.ESCAPE)
# tokyo = driver.find_element(By.XPATH, '//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[6]/div/div/ul/li[1]').click
time.sleep(1)

driver.find_element(By.ID, "check-in-box").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[3]/div[6]/div').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[3]/div[7]/div').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="Tabs-Container"]/button/div/div/span').click()

# 마지막으로 열린 탭으로 전환 이거만 추가하면 됐었는데...
driver.switch_to.window(driver.window_handles[-1])
# print(driver.current_url)

time.sleep(10)

hotels = driver.find_elements(By.CSS_SELECTOR, '.hotel-list-container h3')
price = driver.find_elements(By.CSS_SELECTOR, '.hotel-list-container .PropertyCardPrice__Value')

print(f"호텔명: {hotels[0].text}, 가격: {price[0].text}원")




'''


input("대기")
