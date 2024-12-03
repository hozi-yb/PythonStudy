# 웹 스크래핑

from bs4 import BeautifulSoup
import requests


# html_str = """
# <html>
#     <boby>
#         <div id="content">
#             <ul class="industry">
#                 <li>인공지능</li>
#                 <li>빅데이터</li>
#                 <li>신재생에너지</li>
#             </ul>
#             <ul class="comlang">
#                 <li>Python</li>
#                 <li>C++</li>
#                 <li>Javascript</li>
#         </div>
#     </boby>
# </html>
# """

# soup = BeautifulSoup(html_str, "html.parser")
# print(soup)
# first_ul = soup.find('ul') # find 첫번째로 만나는 태그를 가져옴.
# print(first_ul)
# print(first_ul.text) # 태그 없이 텍스트들만 뽑아옴 / 태그 안에 있는것들을 text라고 한다.
# 
# all_ul = soup.find_all('ul') # 찾는 태그를 다 가져와줌. / 리스트 안에  / findAll <- 옛날방식. 옛날 파이썬, 오류는 아님
# print(all_ul)
# print(all_ul[1])
# print(all_ul[1].text)

# class_ul = soup.find('ul', attrs={'class' : 'comlang'}) #find명령어를 사용해서 원하는 클래스를 가져옴.
# print(class_ul)
# print(class_ul.text)


# select - 선택자를 주로 사용해서 가져온다.

# first_ul = soup.select_one("ul.industry")
# print(first_ul)
# print(first_ul.text)

# all_ul = soup.select("#content > ul")
# print(all_ul)

"""서울시"""
# html_url = "https://seoul.go.kr/main/index.jsp"
# res = requests.get(html_url)
# # print(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# all_nav = soup.select("nav > ul > li > a")
# # print(all_nav[1].text)
# for i in all_nav:
#     print(i.text)

"""국립중앙박물관"""
# html_url = "https://www.museum.go.kr/site/main/home"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')


# info = soup.select(".info-time > li")
# for i in info:
#     print("이용시간 : ", i.text.strip())

# info = soup.select(".info-time > ul > li")
# for i in info:
#     print("관람료 : ", i.text.strip())

# info = soup.select(".btn.btn-over")
# for i in range(2):
#     print(info[i].text, end = " ")

"""kbs 뉴스 스크래핑"""
# html_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8118420"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")

# # print(soup)

# title = soup.select_one(".headline-title")
# print("제목 : ", title.text)

# contents = soup.select_one(".detail-body")
# print("내용 : ", contents.text.strip())

# # 파일저장도 가능하다.
# with open("news.txt", "w", encoding="utf-8") as file:
#     file.write(contents.text.strip())

"""전자신문 스크랩"""
# html_url = "https://www.newsis.com/view/NISX20241203_0002982557"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')

# title = soup.select_one(".tit.title_area")
# print("제목 :", title.text)

# date = soup.select_one(".infoLine > div > p > span")
# print("발행일 :", date.text)

# content = soup.select_one(".viewer article")

# print("\n<<기사>>")

# for i in content:
#     print(i.text.strip())

"""명언출력기"""
# html_url = "https://quotes.toscrape.com/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')

# quote = soup.select(".quote > .text")
# # print(quote)

# # for i in quote:
# #     print(i.text.strip())
# text = [i.text.strip() for i in quote]
# # print(text)

# author = soup.select(".author")
# speaker = [i.text.strip() for i in author]
# # print(speaker)
# # zipped = list(zip(text, speaker))
# # print(zipped)

# for text, speaker in zipped:
#     print(f"말한사람 : {speaker}\n내용 : {text}")
#     print()

#실습 3 환전 고시 환율
# html_url = "https://finance.naver.com/marketindex/?tabSel=exchange"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')

# counties = soup.select(".market1 .data .data_lst h3")
# country = [i.text.strip() for i in counties]
# # print(country)

# market = soup.select(".market1 .data .data_lst .value")
# market_now = [i.text.strip() for i in market]
# # print(market_now)

# zipped = list(zip(country, market_now))
# for country, market_now in zipped:
#     print(f"{country} : {market_now}")

# 실습4 주식정보 스크래핑

html_url = "https://finance.naver.com/item/main.naver?code=373220"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, 'html.parser')

finance_info = soup.select_one(".wrap_company h2")
print("종목:",finance_info.text)

rate_today = soup.select(".rate_info dd")
today = [i.text.strip() for i in rate_today]
for i in today:
    print(i, end = "\n")


rate_info = soup.select(".rate_info table span:not(.blind)")
info = [i.text.strip() for i in rate_info]
for i in info:
    print(f"{i}", end ="")