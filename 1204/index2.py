#selenium

# 셀레늄 기본세팅
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# 셀레늄에서 사용할 메서드들 임포트
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#옵션객체
options = Options()
#옵션추가
# options.add_argument("--start-maximized") # 시작하자마자 창 최대화
options.add_argument("--incognito") # 시크릿모드
#options.add_argument("--headless")

# 크롬드라이버자동설치 및 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options) #이렇게 해주는게 웹드라이버 매니져다.
driver.maximize_window() # 얜 열리고 나서 확대. 옵션으로 하면 그냥 큰 창으로 열려버린다.

driver.get("https://github.com/")
#print(driver.current_url)

# 무한스크롤페이지 스크롤내리기
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.implicitly_wait(5)


#검색창
search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
print(search_input)

# 값 입력
search_input.send_keys("파이썬 코딩연습")
search_input.send_keys(Keys.ENTER)




# #2초뒤 검색어 삭제
time.sleep(2)
# search_input.clear()

# 이메일 / 속성값가져오기
# email_text = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
# href = email_text.get_attribute("href") # attribute로 속성값 가져온다.
# print(href)

driver.save_screenshot("./1204/save.png")

input("대기")
# driver.quit()