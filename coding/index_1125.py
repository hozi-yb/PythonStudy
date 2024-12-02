# 실습. 평균값 구하기
students = {
    "학생1": {"국어": 83, "영어": 92, "수학": 88},
    "학생2": {"국어": 90, "영어": 79, "수학": 86},
    "학생3": {"국어": 88, "영어": 86, "수학": 94}
}

for student, score in students.items():
    # print(student, score)
    total = sum(score.values())  # 세 과목의 합계
    avg = total / len(score)
    # print(avg)
    print(f"{student}의 평균은 {avg:.2f}")

# 이중for문
for i in range(5):
    for j in range(3):
        print(f"i :{i}, j :{j}")
    print()


# 2차원리스트와 for문

matrix = [
    [3, 6, 9, 12],
    [2, 4, 6, 8],
    [10, 20, 30, 40],
    [11, 12, 13, 14]
]
for row in matrix:
    for elem in row:
        if elem % 3 == 0:
            print(elem, end=" ")


# 실습. 이중for문 구구단 만들기
# for i in range(2, 10):
#     print(f"[{i}단]")
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i * j}")
#     print()

# # 실습. 자판기 프로그램
# vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]

# while True:
#     user_input = input("사용자를 선택하세요. (1. 소비자, 2. 주인, 3. 종료): ")

#     if user_input == "1" or user_input == "소비자":
#         drink = input("마시고 싶은 음료는? ")
#         if drink in vending_machine: # 있으면 제거
#             vending_machine.remove(drink)
#             print(f"{drink} 드릴게요")
#         else:
#             print("음료수가 없습니다.")
#         print("남은음료수: ", vending_machine)

#     elif user_input == "2" or user_input == "주인":
#         move = input("할일을 선택하세요. (1. 추가, 2. 삭제): ")
#         if move == "1" or move == "추가":
#             drink = input("추가할 음료수는?")
#             vending_machine.append(drink)
#             print("추가 완료")
#         elif move == "2" or move == "삭제":
#             drink = input("삭제할 음료수는?")
#             if drink in vending_machine:
#                 vending_machine.remove(drink)
#                 print(f"{drink} 삭제 완료")
#             else:
#                 print(f"{drink}는 현재 없습니다.")
#         else:
#             print("값을 잘못입력하셨습니다.")
#         print("남은음료수: ", vending_machine)

#     elif user_input == "3" or user_input == "종료":
#         print("자판기 프로그램을 종료합니다.")
#         break
#     else:
#         print("값을 잘못 입력하셨습니다.")


# 실습. 함수화 하기
def check_machine():
    print("남은음료수: ", vending_machine)


def is_drink(drink):
    return drink in vending_machine


def add_drink(drink):
    vending_machine.append(drink)
    print("추가 완료")


def remove_drink(drink, user):
    if user == "1" or user == "소비자":
        vending_machine.remove(drink)
        print(f"{drink} 드릴게요")
    else:
        vending_machine.remove(drink)
        print(f"{drink} 삭제 완료")


vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]

while True:
    user_input = input("사용자를 선택하세요. (1. 소비자, 2. 주인, 3. 종료): ")

    if user_input == "1" or user_input == "소비자":
        drink = input("마시고 싶은 음료는? ")
        if is_drink(drink):  # drink in vending_machine
            # vending_machine.remove(drink)
            # print(f"{drink} 드릴게요")
            remove_drink(drink, user_input)
        else:
            print("음료수가 없습니다.")
        check_machine()  # print("남은음료수: ", vending_machine)

    elif user_input == "2" or user_input == "주인":
        move = input("할일을 선택하세요. (1. 추가, 2. 삭제): ")
        if move == "1" or move == "추가":
            drink = input("추가할 음료수는?")
            add_drink(drink)
            # vending_machine.append(drink)
            # print("추가 완료")
        elif move == "2" or move == "삭제":
            drink = input("삭제할 음료수는?")
            if is_drink(drink):  # drink in vending_machine:
                remove_drink(drink, user_input)
                # vending_machine.remove(drink)
                # print(f"{drink} 삭제 완료")
            else:
                print(f"{drink}는 현재 없습니다.")
        else:
            print("값을 잘못입력하셨습니다.")
        check_machine()  # print("남은음료수: ", vending_machine)

    elif user_input == "3" or user_input == "종료":
        print("자판기 프로그램을 종료합니다.")
        break
    else:
        print("값을 잘못 입력하셨습니다.")

        # 함수실습1


def multi_or_add(num1, num2):
    if num1 == num2:
        return num1 * num2
    else:
        return num1 + num2


result = multi_or_add(2, 2)
result2 = multi_or_add(2, 3)
print("결과(곱) :", result)
print("결과(합) :", result2)

# 함수실습2


def calc_price(price):
    # total = 0
    fee = 2500
    if price < 20000:
        total = price + fee
    else:
        total = price
    return total


result = calc_price(15000)
result2 = calc_price(30000)
print(f"상품가격은 {result}원")
print(f"상품가격은 {result2}원")


# 함수 매개변수로 리스트 전달
def times(nums):
    return [i ** 2 for i in nums]


number = [2, 3, 6, 9]
print(times(number))
