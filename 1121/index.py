# 변수의 사이즈를 알아보는 방법
from sys import getsizeof

# 우리가 볼 땐 같은 1이지만 컴퓨터가 볼 땐 다르다.
print(getsizeof(1))
print(getsizeof("1"))

# 변수의 자료형 알아보는 방법
print(type(11111)) # class 'int' 인티져
print(type(333.333)) # float
print(type("안녕하세요")) # string
print(type(True)) # bool(불리언) 이라는 참 거짓만 나타내는 자료형
print(type(None)) #NoneType
# 등등... 더 있다.

#형변환
# 그냥 인풋으로 받으면 문자열형태로 받기에
# 형변환이 필요
'''
num = int(input("숫자를 입력하세요. "))
# 문자열로 입력된 값이 숫자로 변환되기만 하면 된다.
# 밑에 num에 int를 붙여도 된다.
a = num % 2 == 0

print("True면 짝수, False면 홀수:", a)
'''
'''
print(int(5.5))
print(int("30"))
a="10"
print(type(int(a)), int(a))

#그럼 데이터의 사이즈는 어떻게 될지?
# getsizeof로 알아보자
'''

# 문자열 연산
print("안녕하세요" + " " + "안녕하세요")
#print("오류" + 1234)
print("hey!" * 10)

a = "python"
# 프린트로 데이터를 확인하기 위해서 보통 사용을 한다.
print("데이터확인" + a)

# 독스트링을 그냥 쓰면 주석처리 한거지만
# 변수와 함께 쓰면 여러 문자열을 출력할 수 있다.
# 독스트링을 쓰는 2가지 이유이다.
korea_song = """
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
"""
print(korea_song)

# 따옴표 출력 ("', '")
print('"오늘 저녁 뭐 먹지?"')
print("'저녁 뭐 먹지'")

# 이스케이프
print("Hello\nWorld") # 줄바꿈
print("Hello\tWorld") # 탭 처리
print("Hello\\World") # 역슬래시 표기
print("It\'s a book") # 홑따옴표 표기
print("\"Hello World\"") # 쌍따옴표 표기


# 문자열 포매팅 / 포맷코드 ( %d, %s 등등)
print("올해는 ")
year = "올해는 %d년 %s의 해이다." % (2025,'뱀띠') # 문자열 포매팅의 한 방식
print(year)

number = "저는 올해 %d살입니다." %(20)
print(number)
calc = "20 나누기 3은 %.2f" %(6.66666)
print(calc)
# 그냥 %f는 소숫점자리 6자리까지 나오는구나.
text = "저는 %s에서 살고있습니다." %"서울"
print(text)
# %10s라고 한다면, 총 10칸을 준다.
# 서울을 포함해서 10칸이니, 공백은 8칸이 된다.
# %-10s 는 뒤로 공백이 채워진다.
char = "이모티콘은 %c 이것으로 할게요" %"👍"
print(char)

country = "대한민국"
city = "서울"
people = "한국인"
text = "저는 올해 {0}살 입니다." .format(20)
print(text)
text = "저는 {0} 사람이며 {1}에 살고있습니다.".format(country, city)
print(text)
text = "제가 사는 {0}은 {a}에 있습니다." .format(city, a="한국")
print(text)
text = "중괄호 출력하고 싶을 때 : {{중괄호}}".format()
print(text)
# 순서를 무조건 지켜서 쓸거다 한다면
text = "{},{},{},{}" .format(80,90,100,200)
print(text)

# 쓰는경우는 많이 없지만 알아둘 것들
a = "[{0:$<10}]".format("hey") 
# :< 우측공백, :> 좌측공백, :^ 가운데정렬
# :$^이라고 한다면, :와 ^중간에 있는 문자가 공백에 채워진다.
print(a)


# 가장 많이쓰게될 f문자열 포맷팅!!!
name = "홍길동"
age = 20
print(f"내 이름은 {name}입니다. 나이는 {age + 1}입니다.")
print(f"내 이름은 {name:*^9}")
print("\n\n")
# 실습. 이스케이프 연습
print("|\\_/|")
print("|q p|     /}")
print("( 0 ) \"\"\" \\")
print("|\"^\"`      | ")
print("| |_/=\\ \\__|")

name = "임유빈"
print(f"[{name:=^53}]")
print(f"문자열 실습입니다. {{ 중괄호 }}를 출력해보세요")

# 문자열 인덱싱
a = "Hello, Python"
print(a[7] + a[8] + a[9] + a[10] + a[11] + a[12]) # ,로 이으면 띄어쓰기가 된다.

# 문자열 슬라이싱
# 식별자[start:end]
# end : 3번인덱스까지 하고싶다면 4번으로해야됨
print(a[7:])

date = "20240930"
year = date[:4]
month = date[4:6]
day = date[6:]
print(year + "년", month + "월", day + "일")

#문자열 길이구하기
print(len(date))

# count 메서드 / 갯수세기
a = "Hello, Python"
print(a.count('l')) # l은 두개있다.

# find 메서드 / 위치 찾기 / 있는지 그냥 찾는 것.
#그래서 없으면 몰라서 -1 나오는 것.
print(a.find('P')) 
print(a.find('s')) # 없으면 -1이 나온다.
print(a.find('o')) # 먼저있는 위치가 나온다.

# 다수일 경우 찾는 방법 / 변수를 이용해야한다.
first_o = a.find('o')
print(first_o)
second_o = a.find('o',first_o + 1)
print(second_o)

# index 메서드 / 위치 찾기 / 어디 인덱스에 있는지 찾는 것
# 그래서 없으면 오류가 난다.
print(a.index('P'))

# print(a.index('q')) 오류

# 바꾸기 나누기 / 굉장히 중요 / 자주씀
# replace 메서드 
a = "Hello, Python"
print(a.replace("Python", "파이썬"))
# split 메서드
print(a.split("o")) # 적은 문자를 기준으로 분리가된다.;

# 대/소문자 바꾸기 / upper, lower 메서드
a = "Hello, World"
print(a.upper()) # 전부 대문자로 바꿔줌
print(a.lower()) # 전부 소문자로 바꿔줌

# 공백지우기 / strip, rstrip, lstrip 메서드
a = "      Hello     "
print(f"[{a.rstrip()}]") # 오른쪽 공백 삭제
print(f"[{a.lstrip()}]") # 왼쪽 공백 삭제
print(f"[{a.strip()}]") # 양쪽 공백 삭제

# 문자열 판별하기(숫자판별) / 음수는 다 false
print("1234".isdecimal()) # r가장 제한적
print("1234".isdigit()) # 가장 많이 씀
print("1234".isnumeric()) # 가장 포괄적

# 문자열 판별하기(문자, 공백판별)
print("hello".isalpha()) # 띄어쓰기 들어가면 안됨

# 문자열 판별하기 (대소문자 판별)
print("Hello".islower())
print("HELLO".isupper())

# 실습 1번 입출력실습
name = input("이름을 입력하세요. ")
age = input("나이를 입력하세요. ")
print(f"안녕하세요! {name}님 ({age}세)")
print("\n")

# 실습 2번 입출력실습
name = input("이름을 입력하세요. ")
age = input("태어난 년도를 입력하세요")
year = input("올해 년도를 입력하세요. ")
age1 = int(year)-int(age)
print(f"올해는 {year}년 {name}님의 나이는 {age1}세 입니다.")

