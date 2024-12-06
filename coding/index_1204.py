# selenium
# from selenium import webdriver

# driver = webdriver.Edge()
# driver.get("https://www.naver.com/")
# print(driver.title)
# driver.quit()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#옵션객체
options = Options()
#옵션추가
options.add_argument("--start-maximized")
options.add_argument("--incognito")
# options.add_argument("--headless")


service = Service()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get("https://google.com")
print(driver.current_url)
# # 무한스크롤페이지 스크롤내리기
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.implicitly_wait(5)

# 검색창
search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]') # //*[@id="APjFqb"]
print(search_input)
#검색어
search_input.send_keys("파이썬 코딩연습")
search_input.send_keys(Keys.ENTER)
# 검색어 삭제
time.sleep(2)
# search_input.clear()
# 속성값가져오기
# email_text = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
# href = email_text.get_attribute("href")
# print(href)

driver.save_screenshot("./1204/save.png")


input("대기")  