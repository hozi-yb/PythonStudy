from bs4 import BeautifulSoup
import requests

#실습3. 환율정보 스크래핑
# html_url = "https://finance.naver.com/marketindex"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")

# usd = soup.select_one("#exchangeList .usd .value")
# print("USD: ", usd.text)

# jpy = soup.select_one("#exchangeList .jpy .value")
# print("JPY: ", jpy.text)

# eur = soup.select_one("#exchangeList .eur .value")
# print("EUR: ", eur.text)

# cny = soup.select_one("#exchangeList .cny .value")
# print("CNY: ", cny.text)

#실습4. 주식정보
# 
# def stock(code):
    # html_url = f"https://finance.naver.com/item/main.naver?code={code}"
    # res = requests.get(html_url)
    # soup = BeautifulSoup(res.text, "html.parser")
# 
    # company = soup.select_one(".wrap_company h2 a")
    # print("회사명:",company.text.strip())
# 
    # price = soup.select_one(".today > .no_today .blind")
    # print("종가:" ,price.text.strip())
# 
    # aprice = soup.select_one(".today .no_exday .blind")
    # print("전일대비:",aprice.text.strip())
# 
# stock("005930")
# stock("294090")

