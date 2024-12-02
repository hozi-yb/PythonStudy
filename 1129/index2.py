"""
# 모듈
#import calc  
#import calc as a # 별칭으로 사용할 수 있다.
#from calc import add, sub # add랑 sub
#from calc import add as a, sub as b
from calc import * # import calc와 전체를 가져온다는 점은 똑같다. import*로 가져오면 하지만 함수 이름으로 바로 가져올 수 있따.

# 모듈명.함수명
print(add(10, 4))
print(sub(10,4))
print(multiply(10,4))
print(divide(10,4))


from datetime import datetime, timedelta, timezone


now = datetime.today() # 현재시간
# today는 타임존이 없다.
#그래서 타임존을 이용한 계산을 할 수 없다.

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print(f"{now.year}년 {now.month}월 {now.day}일")

# 타임존 = 아시아 한국 서울의 시간 이런거
now = datetime.now() # 타임존이 있다.
print(now)
# print(now.year)

# 특정 날짜 계산
next_week = now + timedelta(weeks=1, hours=1)
print(next_week)

# 타임존 계산

print(timezone.utc)
print(datetime.now(timezone.utc)) # now는 타임존 값을 가지고 있다.

print(datetime.now(timezone(timedelta(hours=9))))
# 어디는 utc로 받고 어디는 한국시간으로 받았을 때 같은시간인데 다른시간으로 보일 수 있다. 그 때 시간을 같게 처리하기 위해서 타임존이 필요하다.

from datetime import date

open_day = date(year=2024, month=11, day=18)
print(date.today())
print(date.today().weekday()) # 0부터 시작한 요일의 숫자를 보내준다. weekday
week = ["월", "화", "수", "목", "금","토", "일"]
print(week[date.today().weekday()]) # 이런식으로 요일을 뽑아낼 수 있다.

pass_day = date.today() - open_day
print(pass_day.days)

import time

print(time.time()) # 타임스탬프 값
print(time.localtime()) 

print("2초 대기")
time.sleep(2) # 2 초 동안 프로그램 잠깐 멈춤
print("대기완료")
start = time.perf_counter() # 시간 측정
time.sleep(1)
end = time.perf_counter()
print(end - start)

import math

print(math.pi)
print(math.sqrt(49))
print(math.factorial(5))

print(math.ceil(2.43)) # 올림
print(math.floor(4.88)) # 버림
print(round(2.6)) # 반올림

import random
import math

print(random.randint(1, 10)) # 1~10의 값 랜덤하게 반출,  1 <= a <= 10
print(random.uniform(1.1,9.5)) # 실수를 랜덤하게
print(random.random()) # 0부터 1미만의 값을 난수로 준다.
print(random.randrange(1000, 10000)) # 1000 <= a < 10000
choices = [1,2,3,4,5,6,7,8]
print(random.choice(choices)) # 리스트 안의 값을 랜덤하게 뽑아준다.

# randint나 randrange가 없는 언어는 밑과 같이 여러자리숫자의 난수를 설정해줘야 한다.
rand = 1000 + math.floor(random.random() * 9000)
print(rand)

# 실습. 로또 번호 뽑기

import random

lotto = set()

while len(lotto) < 6:

    lotto.add(random.randint(1,45))
    
print(sorted(lotto))

lotto = random.sample(range(1, 46), 6) # 샘플로 범위설정 가능, 그리고 몇 개 뽑을지도 설정가능

import sys

#print(sys.argv) # 현재 파일의 경로
#print(sys.argv[1:]) # 일단 현재 파일이 있는 경로로 만들어줘야됨. 그러고 python 파일명.py 문자를 띄어서 써주면 리스트 형식으로 들어감..

if "-h" in sys.argv or "--help" in sys.argv:
    print("사용법: python main.py [옵션]")
    print("-h, --help    도움말표시")
    print("-v, --version 버전정보표시")
    sys.exit(0)

if "-v" in sys.argv or "--version" in sys.argv:
    print("버젼 : 1.0.0")
    sys.exit(0)


import os

dir_current = os.getcwd() # 현재위치 알 수 있음 (디렉토리)
print(dir_current)
file_path = os.chdir(dir_current) # os.chdir(디렉토리 경로) : 경로 위치로 이동시킨다.
dir = os.popen('ls') # 명령어, ls : 조회
print(dir.read())

#os.mkdir("test") # 폴더 생성
#os.rmdir("test") # 폴더 삭제
print(os.environ.get('PATH')) # 환경변수를 읽어줌

import json
# 자바스크립트 오브젝트 어쩌구
# 자바 스크립트를 오브젝트로 보내주는 것.
# 자바에서 딕셔너리 형태로 오는데
# 그걸 파이선에서는 그대로 받아서 쓰면 된다.

data = {
    "name": "홍길동",
    "age":20,
    "city":"서울"
}
# 파이썬 객체를 제이슨 문자열로 보내는것.

json_str = json.dumps(data)

print(json_str)

json_obj = json.loads(json_str) # 파이썬 객체로 변환

print(json_obj, json_obj["name"])
"""

# 실습. 타자연습 게임

import random
import time

words = ["mountain", "river", "forest", "ocean", "desert", "tree", "flower", "cloud", "rain", "sunlight"]

while True:

    count_input = input("단어개수를 입력하시오.\n(종료입력시 종료.): ")    

    if count_input == "종료":
        print("게임을 종료합니다.")
        break

    start = time.perf_counter()

    i=0
    while i < int(count_input):

        random_words = random.choice(words)
        words_input = input(f"단어 : {random_words} \n입력 : ")
        
        if words_input != random_words:
            while True:
                
                print("오타! 다시시도하세요.\n")
                words_input = input(f"단어 : {random_words} \n입력 : ")

                if words_input == random_words:
                    i += 1
                    break        
        
        elif words_input == random_words:
            i += 1
            print("통과!")

    end = time.perf_counter()

    print("게임종료!")
    print(f"총 {count_input}개의 단어를 입력하셨습니다. ")
    print(f"총 걸린시간은 {end - start:.2f} 초")
    print(f"평균시간은 {(end-start)/int(count_input):.2f} 초")

    # 함수로 고쳐보자

    
