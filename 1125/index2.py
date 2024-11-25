"""

# 함수

def say_hello(born, name): # 함수 선언!
    age = 2024 - born # born을 사용하기 위해서 위 say_hello로 받아오는 것이다!
    print(f"{name}님의 나이는 {age}세 입니다.")

say_hello(2000, "임유빈") # 2000이 위의 born으로 들어간다.
# 두개면 꼭 두개가 들어가야 한다.
# 두갠데 하나만 넣으면 오류남.
say_hello(2001, "혜린") # 입력값만있고 결과값은 없는 함수이다..

# 곱셈 함수

def gugudan(dan, end): # 1. 함수 정의
    print(f"{dan}단")  # 함수 만들기
    for i in range(1, end + 1): # 속도도 굉장히 빠르다.
        print(f"{dan} x {i} = {dan * i}")

gugudan(4, 20)


# 결과값이 있는 함수?
# return이 있어야 한다.
def calc_sum(num1, num2):
    total = 0
    for i in range(num1, num2 + 1):
        total += i
    return total # return 보내고싶은 값을 써주면 된다.

# return을 받는 애가 필요하다.
result = calc_sum(1, 20) #그래서 변수로 받아줘야된다.
print(result)


# 리스트나 딕셔너리 등으로도 return받을 수 있다.
def fruits():
    return ['사과', '바나나', '복숭아']

print(fruits())

def students():
    return {
        "name" : "홍길동",
        "age" : 20,
        "major" : "컴퓨터공학"
    }
print(students())


# 실습1

def multi_or_sum(a, b):
    if a == b:
        print(f"결과(곱) : {a*b}")
    elif a != b:
        print(f"결과(합) : {a+b}")


multi_or_sum(3,3)
multi_or_sum(3,2)


# 실습2

def calc_price(price, fee):
    if price < 20000:
        total = price + fee
    else:
        total = price
    return total

result = calc_price(40000, 2500)
print(f"상품1 가격: {result}원")
result2 = calc_price(15500, 2500)
print(f"상품2 가격: {result2}원")

# 왠만해서는 리턴하는 습관을 들이자.


# 함수 매개변수로 리스트 전달
def times(nums):
    return [i ** 2 for i in nums]
# 리스트 내포를 사용하는게 빠르고 간단하다.

number = [2 ,3 ,6 ,9 ]
print(times(number))
# 새로운 리스트로 전달된다.


# 실습3. 자판기 프로그램 함수화
# 중복된 코드를 함수화 하는 것이다.
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']


def check_machine():
    return print("남은 음료수 : ", vending_machine)


def is_drink(drink):
    return drink in vending_machine


def add_drink(drink):
    vending_machine.append(drink)
    vending_machine.sort()


def remove_drink(drink):
    if user == "소비자" or user == "1":
        vending_machine.remove(drink)
        print(f"{drink} 드릴게요.")
    else:
        vending_machine.remove(drink)
        print(f"{drink} 삭제 완료")


while True:
    check_machine()
    print()

    user = input("사용자 종류를 입력하세요.\n 1. 소비자\n 2. 사용자\n 3. 나가기\n ")

    if user == "소비자" or user == "1":
        drink = input("마시고 싶은 음료를 고르시오. : ")
        if is_drink(drink):  # 있으면 제거
            remove_drink(drink)

        else:
            print("없음")

    elif user == "사용자" or user == "2":
        user_input = input("추가 or 삭제 선택 : ")

        if user_input == "추가":
            drink = input("추가할 음료수 입력 : ")
            add_drink(drink)

        elif user_input == "삭제":
            drink = input("삭제할 음료 입력 : ")

            if is_drink(drink):
                print(f"{drink}는 현재 없습니다.")

            remove_drink(drink)

        else:
            print("값을 잘못입력하셨습니다.")

    elif user == "나가기" or user == "3":
        print("자판기 프로그램을 종료합니다.")
        break

    else:
        print("잘못입력하셨습니다.")
        print()
"""
