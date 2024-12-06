from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import requests

options = Options()

# options.add_argument("incognito")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com/imghp")

search = driver.find_element(By.ID, 'APjFqb')
cat = search.send_keys("고양이")
search.send_keys(Keys.ENTER)


for i in range(4):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    time.sleep(1)


cat_imgs = driver.find_elements(By.CSS_SELECTOR, 'img.YQ4gaf')
os.makedirs("./1205/cat_img", exist_ok=True)

code = 1
for image in cat_imgs:
    src = image.get_attribute('src')
    # print(src)
    if "https" in src:
        res = requests.get(src)
        
        # print(res.content) 
        # res.content는 이미지나 동영상 값 가져오는 것.
        # res.status_code : 응답코드
        # res.headers : http 헤더의 정보 반환
        # res.url : 최종 url 반환

        with open(f"./1205/cat_img/img_{code}.png", "wb") as file:
            file.write(res.content)
        code += 1




input("대기")