"""
# for문
# 리스트와 for 문
fruits = ["사과", "포도", "바나나", "복숭아"]
for fruit in fruits: # fruits : 반복할 리스트, 리스트내의 개수가 최종숫자가된다.
    print("과일은 : ", fruit) # 리스트 내의 요소가 fruit가 된다.

# 합계구하기
number = [10, 20, 30, 40, 50]
total = 0
for num in number:
    total += num
print(f"리스트 값의 합계는 {total}입니다.")
# 조건문 사용

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in number:
    if num % 2 == 0:
        print(num, end=" ")


# 리스트 내포
squares = [i ** 2  for i in range(1, 20)]
print(squares) # 배열이 만들어진다.

# if문과 함께사용 
even_squares = [i ** 2 for i in range(1, 10) if i % 2 == 0]
print(even_squares)

"""
# 딕셔너리와 for문
my_dict = {
    "name": "홍길동",
    "address": "서울시 은평구",
    "gender": "남자",
    "hobby": ["런닝", "헬스", "낚시"]
}

# i 값이 키값만 순회, 이하 2가지 방법
for i in my_dict:
    print(i)

for i in my_dict.keys():  # 명시적으로 .key를 적어주는게 좋다.
    print(i, end=" ")

print()
print()

# value 순회
for i in my_dict.values():
    print(i, end=" ")

print()
print()

# key, value 같이
# 변수를 두개를 이용하면 튜플이 아닌 값을 바로 뽑을 수 있다.
# key, value가 튜플형식으로 나온다.

for i in my_dict.items():
    print(i, end=" ")

for key in my_dict.keys():
    print(f"{key}: {my_dict[key]}")

for key, value in my_dict.items():
    print(f"{key} : {value}")

"""
"""

# JSON 형태 =  딕셔너리

# 실습. 구구단 만들기
"""
num1 = [1,2,3,4,5,6,7,8,9]
num2 = int(input("몇단을 출력할까요?: "))

for i in num1:
    print(f"{num2} x {i} = {num2*i}" )
"""

# 실습. 정수 합 계산
"""
user_input = int(input("어디까지 계산할까요?: "))
total = 0

for i in range(1, user_input+1, 2):
    total += i
print(f"1부터 {user_input}까지의 홀수의 합은: {total}")


# 실습. 평균값 구하기
total = 0
students = {
    "학생1" : {"국어" : 83,"영어" : 92,"수학" : 88},
    "학생2" : {"국어" : 90, "영어": 79,"수학": 86},
    "학생3" : {"국어" : 88,"영어" : 86,"수학" : 94}
}

for students, score in students.items():
    total = sum(score.values()) # 세 과목의 합계
    avg = total / len(score)
    print(f"{students}의 평균은 {avg:.2f}")


"""
# 이중 for 문
for i in range(5):
    for j in range(3):
        print(f"i : {i}, j : {j}")
    print()

# 2차원 리스트와 for 문

matrix = [
    [3, 6, 9, 12],
    [2, 4, 6, 8],
    [10, 20, 30, 40],
    [11, 12, 13, 14]
]
for row in matrix:
    for element in row:
        if element % 3 == 0:
            print(element, end=" ")


# 실습. 이중 for문 구구단 만들기 / 이중 for문 가장 심플한 예제

for i in range(2, 10):
    print(f"[{i}단]")
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()

"""
# 자판기 프로그램

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

while True:
    print("남은 음료수 : ", vending_machine)
    print()

    user = input("사용자 종류를 입력하세요.\n 1. 소비자\n 2. 사용자\n 3. 나가기\n ")

    if user == "소비자" or user == "1":
        drink = input("마시고 싶은 음료를 고르시오. : ")
        if drink in vending_machine: # 있으면 제거
            vending_machine.remove(drink)
            print(f"{drink} 드릴게요.")
            

        else:
            print("없음")

    elif user == "사용자" or user == "2": # elif대신 if를 쓰는바람에 else가 계속 실행되었다. 주의하자.
        user_input = input("추가 or 삭제 선택 : ")

        if user_input == "추가":
            add_drink = input("추가할 음료수 입력 : ")
            vending_machine.append(add_drink)
            vending_machine.sort() # 오름차순 정렬

        elif user_input == "삭제":
            rm_drink = input("삭제할 음료 입력 : ")

            if rm_drink not in vending_machine:
                print(f"{rm_drink}는 현재 없습니다.")
        
            vending_machine.remove(rm_drink)
            print(f"{rm_drink} 삭제 완료")
        else:
            print("값을 잘못입력하셨습니다.")

    elif user == "나가기" or user == "3":
        print("자판기 프로그램을 종료합니다.")
        break

    else:
        print("잘못입력하셨습니다.")
        print()


"""
"""
if문 조건 만들고 pass처리 하면서 큰 틀을 먼저 만든다.
나가기(break)와 else 만들기.
"""
