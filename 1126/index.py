'''
# 전역변수
quantity = 10 # 상수를 전역변수로 주로 사용한다.
# 하나로 고정된 값.

def get_price(price): # 콜론(:)과 들여쓰기가 하나의 지역이다.
    price = price * quantity   
    return price

print(f"{quantity}개의 가격은 {get_price(2000)}입니다.")

# 지역변수 , 전역이 아닌건 다 지역이라고 봐도 된다.
def one_up(): # 매개변수도 지역변수다.
    x = 0
    x += 1
    return x
print(one_up())

# 유효범위
quantity = 10

def price_sum(price):
    quantity = 7 # 지역변수가 우선적으로 계산된다.
    return price * quantity

print(price_sum(1000))

# 전역변수 값 변경
x = 0

def oneup(): # 지역변수에서 전역변수의 값을 수정할 수 없다.
    global x # global이라는 키워드를 이용해서 x값을 변경할 수 있다.
    x += 1
    return x
print(oneup())
print(oneup())
print(oneup())

# 기본 매개변수
def pr_str(text = "안녕하세요.", count = 1): # 기본매개변수.
    for _ in range(count): # 변수를 선언해야되는데, 안쓰는 경우 _(언더바) 처리한다.
        print(text)

pr_str()
pr_str("hello", 5)
# 순서가 중요하다.
# 순서가 중요한 이유 : 쓸 때 앞 변수를 무조건 먼저 사용해줘야한다.
# text그냥 쓰고 카운트만 바꿀 수 없기 때문
# 하지만 함수 호출키워드를 사용하면 어느정도 순서를 바꿀 수 있다.!

# 함수 호출키워드
def intro(name, age, city):
    print(f"이름은 {name}이고 나이는 {age}이고 사는곳은 {city}입니다.")

intro("홍길동", 23, "서울")
intro(city="서울", name = "임꺽정", age=25) # 순서에 상관없이
intro("홍길동", age=20, city="부산") # 위치 매개변수는 무조건 앞에!!
# 그냥 오류남

# 가변 매개변수
def calc_avg(*args):
    total = 0
    for i in args: # 쓸 땐 그대로 쓰먼 된다. *없이
        total += i
        avg = total / len(args)
    return avg

print(calc_avg(1,2,3,4,5,6,7,8))  # 리스트를 쓸 순 없나? 해보기


def text_def(a,b,*args): # 고정이 무조건 앞에 있어야 한다.
    # 나머지 값이 가변 매개변수에 저장된다.
    print("text : ", a)
    print("b : ",b)
    print("args : ",args)

text_def("hi", 1,2,3,4,5)

def intro(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

intro(name = "홍길동", age = 20, city = "서울", gender = "남자")

# 내장함수
# abs(절대값) - 절대값을 구하는 내장함수
def my_abs(x):  # 절대값 구하는 함수 내가 만들어서 쓰기~
    if x < 0:
        return -x
    else:
        return x
print(my_abs(-10))
print(abs(-10))

# 거듭제곱 만들기
print(pow(2,3))
def my_pow(x,y):
    num = 1
    for i in range(0, y):
        print(f"i = {i} {num} x {x} = {num*x}")
        num *= x
    return num

my_pow(3,4)

# map()

def square(x):
    return x ** 3

numbers = [2,4,6,8]

squared = list(map(square, numbers))# 어차피 리스트에 넣어야되니까 이렇게 쓰는게 일반적. 안넣으면 메모리위치같은거 뜸
print(squared)

# filter()
def even_number(x):
    return x % 2 == 0 # 리턴에 바로 조건을 넣어서 반환하고싶은것만 반환할 수 있다.

numbers = [1,2,3,4,5,6,7,8,9]
print(list(filter(even_number, numbers)))

# return값은 여러개를 한꺼번에 반환할 수 있다.
def get_return():
    arr = ["사과", "바나나"]
    dic = {
        "name" : "홍길동",
        "age" :  20
    }
    num = 30
    return arr, dic, num # 순서대로 넘겨줬기 때문에.
arrs, dics, nums = get_return() # 순서대로 쓰는 것.
print(arrs)
print(dics)
print(nums)

# 실습4. 함수만들기 for, while filter 다 된다. 다 해볼것.
num_list = []
y = int(input("수 입력"))

def filter_number(x):
    return x % y == 0 

for i in range(1, 31):
    num_list.append(i)
    
numbers = list(filter(filter_number, num_list))
print(numbers)
print(f"{y}의 배수의 개수", len(numbers))
# 방법 1
def count(num):
    lists = [ i for i in range(1,31) if i % num == 0]
    counts = len(lists)
    return lists, counts
num = 3
lists, counts = count(num)
print(f"{num}의 배수 : {lists}")
print(f"{num}의 배수의 개수 : {counts}")

# 방법 2
def count(num):
    # 중첩 함수 - 이 함수 내에서만 사용이 가능합니다. / 많이 쓰진 않지만, 개념만..
    def check(x):
        return x % num == 0
    
    lists = list(filter(check, range(1,31))) # 바로 range가 들어가도 된다..
    return lists, len(lists)

num = 3
lists, counts = count(num)
print(f"{num}의 배수 : {lists}")
print(f"{num}의 배수의 개수 : {counts}")

# 재귀함수..
def sos(i):
    print("Help me!", i)
    if i == 1:
        return
    else:
        return sos(i-1)
sos(10)


# 팩토리얼
def factorial(n):
    print("n의 값 : ", n)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# 실습 5. 피보나치 수열 만들기

def fibonacci(i):
    if i== 0:
        return 0 
    elif i==1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2) 

print(fibonacci(6)) # 시간복잡도. 로 보면 좋은 방법은 아니다.

# 람다식 굉장히 많이씀

# 일반함수
def add(x, y):
    return x+y
print(add(2,7))

# 람다식
add = lambda x, y: x+y
print(add(2, 7))

# 매개변수가 하나인 것.
oneup = lambda x : x + 1
print(oneup(1))
print((lambda x : x+1)(1))

square = lambda x : x**2
print(square(4))
print((lambda x : x**2)(4))
#매개변수가 두개인 것.
minus = lambda x,y : x - y
print(minus(10,2))
print((lambda x,y: x-y)(10,2))

# 람다함수를 매개변수로 전달하기. (call_back 함수)
# func이 다른 함수를 불러들임
# func이 콜백함수다
# 람다는 매개변수가 없이 함수를 불러와도 된다.

def call(func):
    for _ in range(10):
        func() # 함수를 받는 것. func만 쓴다면 그냥 변수

def hello():
    print("안녕하세요")

hello2 = lambda: print("반갑습니다.")
call(hello) # 일반 함수
call(hello2) # 람다 함수


numbers = [2, 4, 6, 8]
squared = map(lambda x: x ** 3, numbers)
print(list(squared))

numbers = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x : x % 2 == 0, numbers)))


def count(num):
 
    lists = list(filter(lambda x : x % num == 0, range(1,31)))
    return lists, len(lists)

num = 5
lists, counts = count(num)
print(f"{num}의 배수 : {lists}")
print(f"{num}의 배수의 개수 : {counts}")
'''

# 실습6. 함수 종합 프로그래밍

weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]

def data(i):
    return weather_data[i]
def data2():
    filter_city = list(filter(lambda x: x[1] == city, weather_data))

while True:
    print("[날씨 데이터 분석 프로그램]\n")
    print("1. 평균 기온 계산\n2. 최고/최저 기온 찾기\n3. 강수량 분석\n4. 날씨데이터 추가\n5. 전체 데이터 출력\n6. 종료(임유빈)")
    number = int(input("원하는 기능의 번호를 입력하세요. : "))

    if number == 6:
        print("프로그램을 종료합니다.")
        break

    elif number == 1:
        city = input("도시 이름을 입력하세요: ")    
        filter_city = list(filter(lambda x: x[1] == city, weather_data))
        total = 0
        for i in range(len(filter_city)):
            total += filter_city[i][2]
        avg = total / len(filter_city)
        print(f"{city}의 평균기온 : {avg:.2f}°C")
        print()

    
    elif number == 2:
        city = input("도시 이름을 입력하세요: ")    
        filter_city = list(filter(lambda x: x[1] == city, weather_data)) # 최고/최저 기온 찾기
        temp_list = []
        for i in range(len(filter_city)):
            temp_list.append(filter_city[i][2])
        max_temp = max(temp_list)
        print(max_temp)
        print()
    
    elif number == 3:
        city = input("도시 이름을 입력하세요: ")    
        filter_city = list(filter(lambda x: x[1] == city, weather_data)) # 강수량 분석
        rain_list = []
        for i in range(len(filter_city)):
            rain_list.append(filter_city[i][3])
        total_rain = sum(rain_list)
        print(f"{city}의 총 강수량은 {total_rain}mm")
        print()
    
    elif number == 4: # 날씨 데이터 추가
        date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
        city = input("도시를 입력하세요: ")
        temp = input("평균 기온을 입력하세요 (°C): ")
        rain = input("강수량을 입력하세요 (mm): ")
        weather_data.append([date, city, temp, rain])
        print(f"{city}의 날씨 데이터가 추가되었습니다.")
        print()

    elif number == 5: # 전체 데이터 출력
        for i in range(len(weather_data)):
            print(f"날씨 : {weather_data[i][0]}, 도시 : {weather_data[i][1]}, 평균 기온 : {weather_data[i][2]}, 강수량 : {weather_data[i][3]}")
        print()
    

               
            



    
                    





